# -*- encoding: utf-8 -*-

### import all from app.__init__
from . 	import *
from	flask import 	jsonify, flash, render_template, \
						url_for, make_response, request, redirect, \
						send_file


########################################################################################
# Access token ### from prettyprinted youtube channel
def token_required(f):
	@wraps(f)
	def decorated( *args, **kwargs ):

		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return jsonify({'message' : 'Token is missing!'}), 401

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = User.query.filter_by(public_id=data['public_id']).first()

		except:
			return jsonify({'message' : 'Token is invalid!'}), 401

		return f(current_user, *args, **kwargs)

	return decorated



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INDEX AND LANDING
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():

	time_now	= datetime.datetime.utcnow()

	form = PreRegisterForm()


	### set language

	### check token from session["public_id"] 
	try :
		current_session_uid = session["public_id"]
		# Check_tokens_user ( current_session_uid, lang_set )
	except : 
		current_session_uid = None




	if request.method == 'POST' : #and form.validate_on_submit():

		for f_field in form : 
			log_cis.debug( "form : \n %s \n", pformat(f_field.__dict__) )
			# log_cis.debug( "form name : %s / form data : %s \n", f_field.name, f_field.data )

		return redirect(request.args.get("next") or url_for("index"))




	return render_template( "index.html",

							site_section	= "landing",
							is_landing 		= True, 
							form			= form

							)


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN LOGOUT REGISTER ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# cf : https://runningcodes.net/flask-login-and-mongodb/


@login_manager.user_loader
def load_user(username):

	user = app.config['MONGO_COLL_USERS'].find_one({"email": username})

	if not user :
		
		return None

	return User(user['_id'])




@app.route('/login', methods=['GET', 'POST'])
def login():  

	form = LoginForm()

	if request.method == 'POST' and form.validate_on_submit():

		# log_cis.debug("login / form : %s ", pformat(form.__dict__) ) 

		for f_field in form : 
			# log_cis.debug( "form : \n %s \n", pformat(f_field.__dict__) )
			log_cis.debug( "form name : %s / form data : %s \n", f_field.name, f_field.data )

		user = mongo_users.find_one({"_id": form.userEmail.data})

		if user and User.validate_login(user['password'], form.userPassword.data):

			user_obj = User(user['_id'])
			login_user(user_obj)
			flash("Logged in successfully", category='success')

			return redirect(request.args.get("next") or url_for("index"))

		flash("Wrong username or password", category='error')
	
	return render_template(	'login.html', 
							site_section	= 'login', 
							form			= form,
							# is_landing 	= True

							)




@app.route('/register', methods=['GET', 'POST'])
def register():

	form = RegisterForm()

	if request.method == 'POST':

		# log_cis.debug("login / form : %s ", pformat(form.__dict__) ) 

		for f_field in form : 
			# log_cis.debug( "form : \n %s \n", pformat(f_field.__dict__) )
			log_cis.debug( "form name : %s / form data : %s \n", f_field.name, f_field.data )


		if form.validate_on_submit():

			existing_user = User.objects(email=form.email.data).first()

			if existing_user is None:
				
				hashpass = generate_password_hash(form.password.data, method='sha256')
				new_user = User(form.email.data,hashpass).save()
				login_user(new_user)

				return redirect(url_for('index'))


	return render_template(	'register.html', 
							site_section 	= "register",
							form			= form,
							# is_landing 	= True
							)

	


@app.route('/logout', methods = ['GET'])
def logout():  
	
	logout_user()
	
	return redirect(url_for('login'))





@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():

	return render_template('user_settings.html')



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FILES ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

@app.route('/<file_to_dowload>', methods=['GET'] ) # this is a job for GET, not POST
def download_file(file_to_dowload):
	"""
	
	"""

	return send_file(	'outputs/Adjacency.csv',
						mimetype='text/csv',
						attachment_filename='Adjacency.csv',
						as_attachment=True)