# -*- encoding: utf-8 -*-

### import all from app.__init__
from . 	import *
from	flask 				import 	jsonify, flash, render_template, \
									url_for, make_response, request, redirect, \
									send_file

from 	werkzeug.security 	import 	generate_password_hash, check_password_hash


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### AUTH - TOKEN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

########################################################################################
# Access token ### from prettyprinted youtube channel
"""
def token_required(f):
	@wraps(f)
	def decorated( *args, **kwargs ):

		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return jsonify({'message' : 'Token is missing!'}), 401

		try:
			data 			= jwt.decode(token, app.config['SECRET_KEY'])
			current_user 	= User.query.filter_by(public_id=data['public_id']).first()

		except:
			return jsonify({'message' : 'Token is invalid!'}), 401

		return f(current_user, *args, **kwargs)

	return decorated
"""




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INDEX AND LANDING
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():

	time_now	= datetime.datetime.utcnow()

	form 		= PreRegisterForm()

	### set language

	### check token from session["public_id"] 
	try :
		current_session_uid = session["public_id"]
		# Check_tokens_user ( current_session_uid, lang_set )
	except : 
		current_session_uid = None



	# TO DO 
	if request.method == 'POST' : #and form.validate_on_submit():

		for f_field in form : 
			log_cis.debug( "form : \n %s \n", pformat(f_field.__dict__) )
			# log_cis.debug( "form name : %s / form data : %s \n", f_field.name, f_field.data )

		return redirect(request.args.get("next") or url_for("index"))



	log_cis.debug("current_user : \n %s ", pformat(current_user.__dict__))

	return render_template( "index.html",

							site_section		= "landing",
							is_landing 			= True, 
							form				= form,

							user_infos			= current_user.get_public_infos
						)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN/LOGOUT/REGISTER ROUTES - USING FLASK-LOGIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# cf : https://runningcodes.net/flask-login-and-mongodb/ 
# cf : https://medium.com/@dmitryrastorguev/basic-user-authentication-login-for-flask-using-mongoengine-and-wtforms-922e64ef87fe 
# cf : https://www.youtube.com/watch?v=NYWEf9bZhHQ&t=320s - flask-login and flask-admin


from models import User, AnonymousUser

@login_manager.user_loader
def load_user(userEmail):

	log_cis.debug("userEmail : %s", userEmail)

	user = mongo_users.find_one({ "userEmail" : userEmail })
	log_cis.debug( "user : \n %s", pformat(user)  )

	if not user :
		
		# return None
		return AnonymousUser()

	else :
		# return User( 
		# 				userEmail 		= user['userEmail'],
		# 				userName 		= user['userName'],
		# 				userAuthLevel 	= user['userAuthLevel'] 
		# 			)
		user_ = User()
		user_.populate_user_class_from_dict(user)

		return user_



@app.route('/login', methods=['GET', 'POST'])
def login():  
	""" 
	main page for login
	backed on flask-login classes
	"""

	form = LoginForm()

	if request.method == 'POST' and form.validate_on_submit():

		log_cis.debug("login / reading form ... " ) 
		for f_field in form : 
			log_cis.info( "form name : %s / form data : %s \n", f_field.name, f_field.data )

		user = mongo_users.find_one({"userEmail": form.userEmail.data})
		log_cis.info("user - type : %s - : %s", type(user), pformat(user) )

		if user and User.validate_login( user['userPassword'], form.userPassword.data ):

			log_cis.debug("user found + User.validate_login ")
			
			user_obj = User()
			# user_obj = User( 	
			# 					userEmail 		= user['userEmail'],
			# 					userName 		= user['userName'],
			# 					userAuthLevel 	= user['userAuthLevel'] 
			# 				)
			user_obj.populate_user_class_from_dict(user)

			login_user( user_obj, remember=form.userRememberMe.data )
			
			log_cis.info("Logged in successfully")
			flash("Logged in successfully", category='success')

			return redirect(request.args.get("next") or url_for("index"))

		else :

			flash("Wrong username or password", category='error')
	

	elif request.method == 'GET' : 
	
		return render_template(	'login.html', 
								site_section	= 'login', 
								form			= form,
								# is_landing 	= True

								user_infos		= current_user.get_public_infos

								)




@app.route('/register', methods=['GET', 'POST'])
def register():

	form = RegisterForm()

	if request.method == 'POST':

		print 
		log_cis.info("posting a new user \n")

		# for debugging purposes 
		for f_field in form : 
			log_cis.debug( "form name : %s / form data : %s \n", f_field.name, f_field.data )


		if form.validate_on_submit():

			existing_user = mongo_users.find_one({"userEmail" : form.userEmail.data} )
			
			log_cis.debug("existing_user : %s", pformat(existing_user) )

			if existing_user is None:
				
				# create hashpassword
				hashpass = generate_password_hash(form.userPassword.data, method='sha256')
				log_cis.debug("hashpass : %s", hashpass )
		
				# populate user class
				new_user 	= User( userPassword = hashpass, userAuthLevel="user" )
				new_user.populate_user_class_from_form(userForm=form)
				new_user.check_if_user_structure_is_partner()

				# save user in db
				new_user.insert_to_mongo( coll=mongo_users )

				# logout previous user if any
				logout_user()

				# log user
				login_user(new_user)

				return redirect(url_for('index'))

		else :
			log_cis.error("form was not validated ...")

			return redirect(url_for('register'))

	elif request.method == 'GET':
		
		return render_template(	'register.html', 
								site_section 	= "register",
								form			= form,

								user_infos		= current_user.get_public_infos

								)

	


@app.route('/logout', methods = ['GET'])
def logout():  
	""" 
	simply logout the user with flask_login.logout_user()
	"""
	logout_user()

	log_cis.info("user is logged out...")
	
	return redirect(url_for('index'))




@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():

	return render_template('user_settings.html')



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ADMIN ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


class MyAdminIndexView(AdminIndexView) :

	def is_accessible(self) :
		""" 
		make it accessible via flask-login
		"""
		log_cis.debug("current_user : \n %s", pformat(current_user.__dict__))

		# using custom property class 
		return current_user.is_admin_level # instead of : return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs) :
		
		# TO DO : flash if auth level not enough
		return redirect(url_for('login'))


class UserViewAdmin(ModelView):
	"""
	view of an user in flask-admin
	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
	"""
	
	### for flask-login 

	def is_accessible(self) :
		""" 
		make it accessible via flask-login
		"""

		# using custom property class 
		return current_user.is_admin_level # instead of : return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs) :
		
		# TO DO : flash if auth level not enough

		return redirect(url_for('login'))



	### for flask-admin

	column_list 			= (	
								'userName', 'userSurname', 'userEmail', \
								'userPartnerStructure',
								'userAuthLevel',
								'userHaveProjects',
								'userProfile'
							)
	
	column_sortable_list	= column_list
	# column_sortable_list 	= (	'userName', 'userSurname', 'userEmail', \
	# 							'structure',)
	
	# column_filters = (BooleanEqualFilter(column=UserID.userName, name='userName'),)

	form 					= UserAdminInfos




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