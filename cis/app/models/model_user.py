# -*- encoding: utf-8 -*-


from flask_login 		import UserMixin, AnonymousUserMixin

from werkzeug.security 	import check_password_hash

from .. import log_cis, pformat


class AnonymousUser(AnonymousUserMixin):
	"""
	anonymous user for flask-login
	cf : https://stackoverflow.com/questions/19274226/how-to-track-the-current-user-in-flask-login
	"""

	def __init__(self):

		log_cis.debug("creating AnonymousUser")

		self.userName 		= 'Guest'
		self.userAuthLevel	= 'visitor'

	@property
	def get_public_infos(self):
		
		return { 	
					"userName" 			: self.userName, 
					"userAuthLevel" 	: self.userAuthLevel,
					"is_authenticated" 	: self.is_authenticated
				}


class User( UserMixin ):

	def __init__(self, 	userName		= None,
						userEmail		= None, 
						userPassword	= None,
						userAuthLevel	= "visitor",
						userRememberMe	= True,
						):
		"""
		datamodel for a user in CIS_front
		- includes a UserMixin from flask-login
		- take care of keeping same 
		"""

		log_cis.debug("creating User")

		# session and auth variables

 		self.userRememberMe 		= userRememberMe

 		self.userEmail 				= userEmail
 		self.userAuthLevel 			= userAuthLevel
 		self.userPassword 			= userPassword
 		self.userPublicKeyAPI 		= None


		# infos variables

 		self.userName 				= userName
 		self.userSurname 			= None
 		self.userProfile 			= None


		# collective related variables

 		self.userHaveProjects		= None
 		self.userJoinCollective 	= None
 		self.userMessage 			= None

 		self.userPartnerStructure 	= None
		self.userOtherStructure		= None
 		self.userStructureProfile 	= None
 		self.userStructureSiret 	= None


		# log user

 		self.userCreatedAt 			= None
 		self.userModifiedAt 		= None

	def populate_user_class_from_form(self, userForm=None) : 
		"""
		retrieve register or preregister form (from .forms) 
		"""

		for f_field in userForm : 
			if f_field.name not in [ "userPassword", "userConfirmPassword", "csrf_token" ] :
				"""
				do not save password here : 
				password needs to be hashed and should be initialized at __init__
				"""
				log_cis.debug("f_field.name : %s / f_field.data: %s ", f_field.name, f_field.data)
				self.__dict__[ f_field.name ] = f_field.data


	def populate_user_class_from_dict(self, userDict=None) : 
		"""
		populate User class from dict (as from pymongo query)
		"""
		for k,v in userDict.iteritems() :
			self.__dict__[ k ] = v


	@property
	def is_admin_level(self):
		return self.userAuthLevel == "admin"

	@property
	def get_public_infos(self):
		
		return { 	
					"userName" 			: self.userName, 
					"userAuthLevel" 	: self.userAuthLevel,
					"is_authenticated" 	: self.is_authenticated
				}

	# TO DO 
	def check_if_user_structure_is_partner(self) :
		pass

	# TO DO 
	def create_jwt_token(self):
		pass 

	# TO DO 
	def create_API_key(self):
		pass

	def insert_to_mongo(self, coll=None ):
		"""
		save model as document in mongoDB
		"""
		
		# convert object to dict
		user_as_dict = self.__dict__
		log_cis.debug("user_as_dict : \n %s", pformat(user_as_dict))

		# save it to collection
		coll.insert( user_as_dict )

	# TO DO 
	def update_existing_user(self):
		pass

	# def is_authenticated(self):
	# 	return True

	# def is_active(self):
	# 	return True

	# def is_anonymous(self):
	# 	return False

	def get_auth_level(self):
		return self.userAuthLevel


	def get_id(self):
		return self.userEmail

	@staticmethod
	def validate_login(password_hash, password):
		return check_password_hash(password_hash, password)
