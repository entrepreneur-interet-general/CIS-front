#!/usr/bin/env python
# -*- encoding: utf-8 -*-

### good encoding of flash messages
### cf : https://stackoverflow.com/questions/8924014/how-to-handle-my-unicodedecodeerror 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
### ERRORS HANDLERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


@app.errorhandler(404)
def error404(error):

	log_cis.error( "error - 404 : %s", error )
	
	form 			= FeedbackForm()
	
	return render_template( "errors.html",

							config_name			= config_name, # prod or default...
							app_metas			= app_metas, 
							language			= "fr" ,
							languages_dict		= app_languages_dict ,

							site_section		= "404",
							error_msg			= u"la page demandée n'existe pas",
							user_infos			= current_user.get_public_infos,
							form				= form
						),404

@app.errorhandler(500)
def error500(error):

	log_cis.error( "error - 500 : %s", error )

	form 			= FeedbackForm()
	
	return render_template( "errors.html",

							config_name			= config_name, # prod or default...
							app_metas			= app_metas, 
							language			= "fr" ,
							languages_dict		= app_languages_dict ,

							site_section		= "500",
							error_msg			= u"erreur serveur",
							form				= form,
							user_infos			= current_user.get_public_infos
						),500

@app.errorhandler(403)
def error403(error):

	log_cis.error( "error - 403 : %s", error )

	form 			= FeedbackForm()
	
	return render_template( "errors.html",

							config_name			= config_name, # prod or default...
							app_metas			= app_metas, 
							language			= "fr" ,
							languages_dict		= app_languages_dict ,
							
							site_section		= "403",
							error_msg			= u"accès interdit",
							form				= form,
							user_infos			= current_user.get_public_infos
						),403




# V3 Website

@app.route('/', methods=['GET'])
def home():

	log_cis.debug("entering new home page")
	
	form 			= FeedbackForm()

	return render_template(
		"new-home.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr", 
		form				= form
	)


@app.route('/en', methods=['GET'])
def home_english():

	log_cis.debug("entering new home page in English")
	
	form 			= FeedbackForm()

	return render_template(
		"new-home-english.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "en", 
		form				= form
	)







@app.route('/recherche', methods=['GET'])
@app.route('/project/<id>', methods=['GET'])
def spa(id=''):

	log_cis.debug("entering SPA page")

	return render_template(
		"spa.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)






@app.route('/le-projet', methods=['GET'])
def leProjet():

	log_cis.debug("entering le projet page")

	return render_template(
		"le-projet.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)


@app.route('/the-project', methods=['GET'])
def theProject():

	log_cis.debug("entering theProject page")

	return render_template(
		"le-projet-english.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "en" 
	)


@app.route('/le-projet/outils', methods=['GET'])
def lesOutils():

	log_cis.debug("entering les outils page")

	return render_template(
		"les-outils.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)

@app.route('/the-project/tools', methods=['GET'])
def theTools():

	log_cis.debug("entering tools page")

	return render_template(
		"les-outils-english.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "en" 
	)


@app.route('/le-projet/parlent-de-nous', methods=['GET'])
def presse():

	log_cis.debug("entering presse page")

	return render_template(
		"parlent-de-nous.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)

@app.route('/le-projet/recompenses', methods=['GET'])
def recompenses():

	log_cis.debug("entering recompenses page")

	return render_template(
		"recompenses.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)

@app.route('/the-project/rewards', methods=['GET'])
def rewards():

	log_cis.debug("entering rewards page")

	return render_template(
		"recompenses-english.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "en" 
	)






@app.route('/qui-sommes-nous', methods=['GET'])
def quiSommesNous():

	log_cis.debug("entering qui-sommes-nous page")

	return render_template(
		"le-collectif.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)

@app.route('/qui-sommes-nous/qui-fait-quoi', methods=['GET'])
def leCollectif():

	log_cis.debug("entering qui-fait-quoi page")

	return render_template(
		"qui-fait-quoi.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr" 
	)

@app.route('/nous-rejoindre', methods=['GET'])
def nousRejoindre():

	log_cis.debug("entering nous-rejoindre page")

	referencedProjectCarrierForm = ReferencedProjectCarrierForm()


	return render_template(
		"nous-rejoindre.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr",
		referencedProjectCarrierForm = referencedProjectCarrierForm
	)

@app.route('/contact', methods=['GET'])
def contact():
	
	form = FeedbackForm()

	log_cis.debug("entering contact page")

	return render_template(
		"contact.html",
		config_name			= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		language			= "fr",
		form 				= form
	)


@app.route('/feedback', methods=['POST'])
def feedback():

	log_cis.debug("entering feedback endpoint")
	
	form 			= FeedbackForm()

	try :
		current_session_uid = session["public_id"]
		# Check_tokens_user ( current_session_uid, lang_set )
	except : 
		current_session_uid = None


	if form.validate_on_submit():

		### ADD A NEW FEEDBACK
		# create preregister data and store it in MongoDB
		new_preregister 	= PreRegister()
		new_preregister.populate_from_form( form=form )
		new_preregister.add_created_at()
		new_preregister.insert_to_mongo( coll=mongo_feedbacks )

		# check if email/user already exists in users db
		# existing_user 		= mongo_users.find_one({"userEmail" : form.userEmail.data} )
		
		# create a potential user if doesn't already exist in db
		# if not existing_user :
			
		# 	# create default password
		# 	temp_pwd = pwd_generator()
		# 	hashpass = generate_password_hash( temp_pwd, method='sha256')
	
		# 	# capitalize name and surname 
		# 	form.userName.data 		= form.userName.data.capitalize()
		# 	form.userSurname.data 	= form.userSurname.data.capitalize()

		# 	# populate user class
		# 	new_user 	= User( userPassword = hashpass, userAuthLevel="visitor", temp_pwd=temp_pwd )
		# 	new_user.populate_from_form(form=form)
		# 	new_user.add_created_at()
		# 	new_user.check_if_user_structure_is_partner()

		# 	# save user in db as visitor
		# 	new_user.insert_to_mongo( coll=mongo_users )
		
		flash(u"votre message a bien été envoyé, merci de votre intérêt !", category='primary')

	else :
		
		log_cis.error("form was not validated / form.errors : %s", form.errors )
		
		flash(u"problème lors de l'envoi de votre message", category='warning')

		
	return redirect(request.referrer or "/")


		
@app.route('/nous-rejoindre/porteur-projet-reference', methods=['POST'])
def porteurProjetReference():

	log_cis.debug("entering /nous-rejoindre/porteur-projet-reference endpoint")
	
	form = ReferencedProjectCarrierForm()
		
	### for debugging purposes
	for f_field in form : 
		log_cis.debug( "preregister form name : %s / form data : %s", f_field.name, f_field.data )


	if form.validate_on_submit():

		log_cis.debug("form validated")
		### ADD A NEW JOIN US ENTRY
		referencedProjectCarrierFeedback = ModelMixin()
		referencedProjectCarrierFeedback.populate_from_form( form=form )
		referencedProjectCarrierFeedback.add_created_at()
		referencedProjectCarrierFeedback.insert_to_mongo( coll=mongo_join_message_referenced_project_carrier )

	else :
		
		log_cis.debug("form was not validated / form.errors : %s", form.errors )

		
	return redirect(request.referrer or "/")








### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN/LOGOUT/REGISTER ROUTES - USING FLASK-LOGIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# cf : https://runningcodes.net/flask-login-and-mongodb/ 
# cf : https://medium.com/@dmitryrastorguev/basic-user-authentication-login-for-flask-using-mongoengine-and-wtforms-922e64ef87fe 
# cf : https://www.youtube.com/watch?v=NYWEf9bZhHQ&t=320s - flask-login and flask-admin


from models import User, AnonymousUser

@login_manager.user_loader
def load_user(userEmail):	
	"""
	populates the current_user flask_login object
	"""

	log_cis.debug("userEmail : %s", userEmail)

	user = mongo_users.find_one({ "userEmail" : userEmail })
	# user = mongo_users.find_one({ "_id" : ObjectId(userOID) })

	if not user :
		
		log_cis.debug( "no user found in db" )
		
		# return None
		return AnonymousUser()

	else :
		
		log_cis.debug( "user : \n %s", pformat(user)  )
		log_cis.debug( "user['_id'] : %s", str(user["_id"]) )

		user_ = User( )
		user_.populate_from_dict(dict_input=user)
		
		### adds forgotten OID into current_user
		user_.userOID = str(user["_id"])

		return user_



@app.route('/login', methods=['GET', 'POST'])
def login():  
	""" 
	main page for login
	backed on flask-login classes
	"""

	form = LoginForm()

	if request.method == 'POST' :

		log_cis.debug("login / reading form ... " ) 
		for f_field in form : 
			log_cis.info( "form name : %s / form data : %s \n", f_field.name, f_field.data )


		if form.validate_on_submit():

			user = mongo_users.find_one({"userEmail": form.userEmail.data})
			log_cis.info("user - type : %s - : %s", type(user), pformat(user) )

			if user and User.validate_login( user['userPassword'], form.userPassword.data ):

				log_cis.debug("user found + User.validate_login ")
				
				user_obj = User()
				user_obj.populate_from_dict(dict_input=user)
				
				### login with flask-login
				login_user( user_obj, remember=form.userRememberMe.data )
				
				### update login_last_at in db
				user["login_last_at"] 	= datetime.datetime.now()
				user["logins_total"]	= user["logins_total"] + 1
				mongo_users.save(user)

				log_cis.info("Logged in successfully")

				# flash(u"Vous êtes bien connecté.e", category='light')

				return redirect(request.args.get("next") or url_for("home"))

			else : 

				log_cis.error("password was not validated / form.errors : %s", form.errors )

				flash(u"Email ou mot de passe incorrect(s)", category='warning')

				return redirect(url_for("login"))

		else :

			log_cis.error("form was not validated / form.errors : %s", form.errors )

			flash(u"Email ou mot de passe incorrect(s)", category='warning')

			return redirect(url_for("login"))


	elif request.method == 'GET' : 
		
		return render_template(	'login.html', 

								config_name		= config_name, # prod or default...
								app_metas		= app_metas, 
								language		= "fr" ,
								languages_dict	= app_languages_dict ,

								site_section	= 'login', 
								form			= form,
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
			log_cis.debug( "form name : %s / form data : %s ", f_field.name, f_field.data )


		if form.validate_on_submit():

			# capitalize name and surname 
			form.userName.data 		= form.userName.data.capitalize()
			form.userSurname.data 	= form.userSurname.data.capitalize()

			existing_user = mongo_users.find_one({"userEmail" : form.userEmail.data} )
			
			log_cis.debug("existing_user : %s", pformat(existing_user) )

			
			if existing_user is None : 
				is_new_user = "create_new_user"
			else : 
				if existing_user["userAuthLevel"] == "visitor" :
					is_new_user = "update_visitor_to_user"
				else :
					is_new_user = "no" 
					flash(u"Cet email est déjà utilisé, veuillez réessayer", category='warning')
					return redirect(url_for('register'))

			log_cis.warning("is_new_user : %s", is_new_user )

			# if existing_user is None or existing_user["userAuthLevel"] == "visitor" :
			if is_new_user != "no" :
				
				# create hashpassword
				hashpass = generate_password_hash(form.registerPassword.data, method='sha256')
				log_cis.debug("hashpass : %s", hashpass )
		
				# populate user class
				new_user 	= User( 	userPassword=hashpass, 
										userAuthLevel="user",
										login_last_at=datetime.datetime.now(),
										logins_total=1
										 )
				new_user.populate_from_form(form=form)
				new_user.add_created_at()

				# check if user declared being from a partner and set 'verified_as_partner' as 'VERIFY
				new_user.check_if_user_structure_is_partner()


				if is_new_user == "create_new_user":
					# save user in db --> function from ModelMixin
					log_cis.warning("inserting new_user in mongo_users" )
					new_user.insert_to_mongo( coll=mongo_users )
				
				# else : # equivalent to <-- 
				if is_new_user == "update_visitor_to_user" :
					# update visitor to user in db --> function from ModelMixin
					log_cis.warning("updating new_user in mongo_users" )
					new_user.update_document_in_mongo( document=existing_user,  coll=mongo_users )


				# logout previous user if any
				logout_user()

				# log user with flask-login
				login_user(new_user)




				flash(u"Votre compte a bien été créé", category='success')

				return redirect(url_for('home'))

		else :
			
			log_cis.error("form was not validated : form.errors : %s", form.errors )

			# flash(u"Problème lors de l'envoi de votre formulaire.<br>Merci de réessayer", category='warning')

			for k,errors in form.errors.iteritems() :
				for e in errors : 
					flash( e , category='danger')

			return redirect(url_for('register'))


	elif request.method == 'GET':
		
		return render_template(	'register.html', 

								config_name		= config_name, # prod or default...
								app_metas		= app_metas, 
								language		= "fr" ,
								languages_dict	= app_languages_dict ,

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
	
	flash(u"Vous êtes maintenant déconnecté.e", category='primary')

	return redirect(url_for('home'))




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER PREFERENCES ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


### TO DO 
@app.route('/preferences/user_infos', methods=['GET', 'POST'])
@login_required
def pref_infos():
	"""
	to update user infos
	"""

	form = UserParametersForm()

	# print current_user


	if request.method == 'POST' :

		print 
		log_cis.info("updating an user - POST \n")

		# for debugging purposes 
		for f_field in form : 
			log_cis.info( "form name : %s / form data : %s ", f_field.name, f_field.data )

		
		if form.validate_on_submit():

			existing_user = mongo_users.find_one({"_id" : ObjectId(form.userOID.data)} )
			log_cis.debug("existing_user : %s", pformat(existing_user) )


			### check if new email is already used by someone else
			is_new_email_taken = False
			existing_email = mongo_users.find_one( {"userEmail" : form.userEmail.data} )
			log_cis.debug("existing_email : %s", pformat(existing_email) )
			if existing_email is not None : 
				if existing_user["_id"] != existing_email["_id"] : 
					is_new_email_taken = True 
		
			if existing_user is None :
				flash(u"Erreur : utilisateur inexistant", category='warning')
				return redirect(url_for('pref_infos'))

			if is_new_email_taken : 
				flash(u"Erreur : cet email déjà utilisé", category='warning')
				return redirect(url_for('pref_infos'))

			else : 

				### saving updated infos in user
				user_obj = User()
				user_obj.populate_from_dict(dict_input=existing_user)

				# # update visitor to user in db --> function from ModelMixin
				log_cis.warning("updating new_user in mongo_users" )
				
				user_obj.populate_from_form( form=form )
				user_obj.update_document_in_mongo( document=existing_user, coll=mongo_users )
				
				### relog user
				login_user( user_obj, remember=existing_user['userRememberMe'] )

				flash(u"Vos informations ont bien été mises à jour", category='primary')
				return redirect(url_for('pref_infos'))
		
		else : 
			
			log_cis.error("form was not validated : form.errors : %s", form.errors )

			flash(u"Erreur : formulaire invalide", category='warning')
			return redirect(url_for('pref_infos'))


	elif request.method == 'GET' :

		log_cis.info("updating an user - GET \n")
		
		print current_user.__dict__

		# prepopulate input fields 
		form.userOID.data 				= str(current_user.userOID)
		form.userName.data 				= current_user.userName.capitalize()
		form.userSurname.data 			= current_user.userSurname.capitalize()
		form.userEmail.data 			= current_user.userEmail
		form.userOtherStructure.data 	= current_user.userOtherStructure	

		# prepopulate select fields
		form.userProfile.process_data(current_user.userProfile)
		form.userPartnerStructure.process_data(current_user.userPartnerStructure)
		form.userStructureProfile.process_data(current_user.userStructureProfile)

		# prepopulate boolean fields
		form.userHaveProjects.process_data(current_user.userHaveProjects)
		form.userJoinCollective.process_data(current_user.userJoinCollective)
		form.userNewsletter.process_data(current_user.userNewsletter)


		return render_template('user_preferences/user_parameters.html',
								
								config_name		= config_name, 						# prod or default...
								app_metas		= app_metas, 
								language		= "fr" ,
								languages_dict	= app_languages_dict ,

								site_section 	= "preferences",
								site_subsection = "infos",
								form			= form,
								user_infos		= current_user.get_public_infos 	# cf model_user.py
								
								)


@app.route('/preferences/user_password', methods=['GET', 'POST'])
@login_required
def pref_password():
	"""
	to update user infos
	"""

	form = UserNewPassword()

	# print current_user


	if request.method == 'POST' :

		print 
		log_cis.info("updating user password \n")

		# for debugging purposes 
		for f_field in form : 
			log_cis.info( "form name : %s / form data : %s ", f_field.name, f_field.data )

		if form.validate_on_submit():

			existing_user = mongo_users.find_one({"_id" : ObjectId(form.userOID.data) } )
			# existing_user = mongo_users.find_one({"userEmail" : form.userEmailHidden.data} )

			log_cis.debug("existing_user : %s", pformat(existing_user) )

			if existing_user is None : 
				flash(u"Erreur : utilisateur inexistant", category='warning')
				return redirect(url_for('pref_password'))

			else : 

				### check if old password is correct 
				log_cis.info ( "checking oldPassword : ", User.validate_login( existing_user['userPassword'], form.oldPassword.data ) )

				### update password / create new hashpassword
				new_hashpass = generate_password_hash(form.newPassword.data, method='sha256')
				log_cis.debug("new_hashpass : %s", new_hashpass )

				### saving new password in user
				user_obj = User()
				user_obj.populate_from_dict(dict_input=existing_user)
				user_obj.userPassword = new_hashpass

				### TO DO 
				# # update visitor to user in db --> function from ModelMixin
				log_cis.warning("updating user_obj in mongo_users" )

				user_obj.update_document_in_mongo( document=existing_user, coll=mongo_users )

				### re-log user
				### login with flask-login
				login_user( user_obj, remember=existing_user['userRememberMe'] )


				flash(u"Votre mot de passe a  bien été mis à jour", category='primary')
				return redirect(url_for('pref_password'))
		
		else : 
			
			log_cis.error("form was not validated : form.errors : %s", form.errors )

			flash(u"Erreur : formulaire invalide", category='warning')
			return redirect(url_for('pref_password'))


	elif request.method == 'GET' :

		# prepopulate input fields 
		form.userOID.data 				= current_user.userOID
		# form.userEmailHidden.data 	= current_user.userEmail
		
		return render_template('user_preferences/user_parameters.html',
								
								config_name		= config_name, 						# prod or default...
								app_metas		= app_metas, 
								language		= "fr" ,
								languages_dict	= app_languages_dict ,

								site_section 	= "preferences",
								site_subsection = "password",
								form			= form,
								user_infos		= current_user.get_public_infos 	# cf model_user.py
								
								)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ADMIN ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### to customize admin views check : https://www.youtube.com/watch?v=BIcjT2Zz4bU

### flask-admin formatters
### cf : http://flask-admin.readthedocs.io/en/latest/api/mod_model/#flask_admin.model.BaseModelView.column_type_formatters 

def date_format(view, value):
	return value.strftime('%d.%m.%Y')

MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({
		type(None): typefmt.null_formatter,
		date: date_format
	})

class CustomWidget(XEditableWidget):
	def get_kwargs(self, subfield, kwargs):
		if subfield.type == 'TextAreaField':
			kwargs['data-type'] = 'textarea'
			kwargs['data-rows'] = '20'
		# elif: kwargs for other fields

		return kwargs

class MyAdminIndexView(AdminIndexView) :

	def is_accessible(self) :
		""" 
		make it accessible via flask-login
		"""
		log_cis.debug("current_user : \n %s", pformat(current_user.__dict__))

		# using custom property class 
		return current_user.is_staff_level # instead of : return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs) :
		
		# TO DO : flash if auth level not enough
		flash(u"Vous ne pouvez pas accéder à cette section", category='warning')
		return redirect(url_for('home'))

class UserViewAdmin(ModelView):
	"""
	view of an user in flask-admin
	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
	"""
	### for flask-login 
	column_type_formatters = MY_DEFAULT_FORMATTERS

	list_template 	= 'admin/list.html'
	create_template = 'admin/create.html'
	edit_template 	= 'admin/edit.html'

	can_export = True
 	can_set_page_size = True

	def is_accessible(self) :
		""" 
		make it accessible via flask-login
		"""

		# using custom property class 
		return current_user.is_admin_level # instead of : return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs) :
		
		# TO DO : flash if auth level not enough
		flash(u"Vous ne pouvez pas accéder à cette section", category='warning')

		return redirect(url_for('home'))

	def get_list_form(self):
		return self.scaffold_list_form(widget=CustomWidget)

	### for flask-admin

	column_list 			= (	
								'userName', 'userSurname', 'userEmail', 
								'userProfile',
								# 'last_modified_at', 
								'logins_total',
								'userPartnerStructure', 'userOtherStructure','verified_as_partner',
								'userAuthLevel', 
								'userHaveProjects','userJoinCollective',
								'userMessage', 
								'follow_up_user',
								# 'created_at', 
								'login_last_at',
							)
	column_details_list = column_list + ('created_at', 'last_modified_at', '_id')
	can_view_details = True

	column_searchable_list 		= ( 'userName', 'userSurname', 'userEmail', 
									'userPartnerStructure', 'userOtherStructure',
									'verified_as_partner',
									'userProfile',
									'userAuthLevel', 
									)
	column_sortable_list	= column_list
	# column_sortable_list 	= (	'userName', 'userSurname', 'userEmail', 
	# 							'userPartnerStructure','userOtherStructure'
	# 							)
	
	# column_filters = (BooleanEqualFilter(column=UserID.userName, name='userName'),)

	
	column_labels = dict(	userName				= 'Name', 
							userSurname				= 'Last Name',
							userEmail				= 'Email',
							userProfile				= 'Profile',
							userPartnerStructure	= 'Structure (partner)',
							userOtherStructure		= 'Structure (other)',
							userAuthLevel			= 'Auth Level',
							userHaveProjects		= 'Have Projects',
							userJoinCollective		= 'Wants to join collective',
							userMessage				= 'Message',
							follow_up_user			= 'Suivi',

						)

	form 					= UserAdminInfos

	# custom field rendering in admin interface 
	# cf : https://stackoverflow.com/questions/21727129/how-to-make-a-field-non-editable-in-flask-admin-view-of-a-model-class 
	form_widget_args = {
		'userEmail'			: { 'readonly' : True },
		'created_at'		: { 'readonly' : True },
		'userPublicKeyAPI'	: { 'readonly' : True },
		'temp_pwd'			: { 'readonly' : True },
	}


class FeedbackAdmin(ModelView):
	"""
	view of a message in flask-admin
	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
	"""
	
	### for flask-login 
	column_type_formatters = MY_DEFAULT_FORMATTERS

	list_template 	= 'admin/list.html'
	create_template = 'admin/create.html'
	edit_template 	= 'admin/edit.html'

	can_export = True
 	can_set_page_size = True

	def is_accessible(self) :
		""" 
		make it accessible via flask-login
		"""
		# using custom property class 
		# return current_user.is_admin_level # instead of : return current_user.is_authenticated
		return current_user.is_staff_level # instead of : return current_user.is_authenticated

	def inaccessible_callback(self, name, **kwargs) :
		
		# TO DO : flash if auth level not enough

		return redirect(url_for('home'))


	### for flask-admin

	column_list 			= (	
								'userName', 'userSurname', 'userEmail', 
								'userOtherStructure', 
								'userFeedbackTopic',
								'userMessage',
								'created_at',
								'follow_up_user'
							)
	column_searchable_list 		= column_list
	column_sortable_list	= column_list

	column_labels = dict(	userName				= u'Prénom', 
							userSurname				= u'Nom',
							userEmail				= u'Email',
							userOtherStructure		= u'Structure',
							userFeedbackTopic		= u'Sujet',
							userMessage				= u'Message',
							follow_up_user			= u'Suivi',
							created_at				= u'Reçu le'
						)

	form 					= MessagesFromLandingAdmin

	# custom field rendering in admin interface 
	form_widget_args = {
		'userEmail'	: {'readonly': True},
		'created_at': {'readonly': True },
	}



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FILES ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


@app.route('/download/<file_ext>/<file_name>', methods=['GET'] ) # this is a job for GET, not POST
def download_file(file_ext, file_name):
	"""
	send file from server
	"""

	log_cis.debug("file_name : %s ", 	file_name)
	log_cis.debug("file_ext : %s ", 	file_ext)
	log_cis.info("file_ext in AUTHORIZED_FILETYPES_LIST: %s", (file_ext in AUTHORIZED_FILETYPES_LIST) )


	if file_ext in AUTHORIZED_FILETYPES_LIST : 

		file_mimetype 		= AUTHORIZED_FILETYPES_DICT[file_ext]["mimetype"]
		file_foldername 	= AUTHORIZED_FILETYPES_DICT[file_ext]["folder"]
		file_folder 		= "static/{}/".format(file_foldername)
		file_name_ext 		= "{}.{}".format(file_name, file_ext) 
		full_filepath 		= file_folder + file_name_ext

		try : 

			return send_file(	full_filepath,
								mimetype			= file_mimetype,
								attachment_filename	= file_name_ext,
								as_attachment		= True
							)
		except :
			
			log_cis.error("downloading this file is not working: %s.%s ", file_name, file_ext )
			
			return redirect(url_for('home'))

	else :

		log_cis.error("downloading this file is not authorized: %s.%s ", file_name, file_ext )

		return redirect(url_for('home'))
