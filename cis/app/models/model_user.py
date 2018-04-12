# -*- encoding: utf-8 -*-


from flask_login 		import UserMixin, AnonymousUserMixin

from werkzeug.security 	import check_password_hash

from . 	import FORM_FIELDS_TO_IGNORE, ModelMixin, time, datetime

from .. import log_cis, pformat

from ..settings.app_choices import * 


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

	@property
	def is_admin_level(self):
		return False

	@property
	def is_staff_level(self):
		return False


class User( UserMixin, ModelMixin ):


	def __init__(self, 	userName		= None,
						userEmail		= None, 
						userPassword	= None,
						userAuthLevel	= "visitor",
						userRememberMe	= True,

						temp_pwd		= None,

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


		# just for preregister

		self.temp_pwd				= temp_pwd


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


	@property
	def is_admin_level(self):
		return self.userAuthLevel == "admin"

	@property
	def is_staff_level(self):
		return self.userAuthLevel in ["admin", "staff"]


	@property
	def get_public_infos(self):
		
		return { 	
					"userName" 			: self.userName, 
					"userAuthLevel" 	: self.userAuthLevel,
					"is_authenticated" 	: self.is_authenticated
				}

	def get_auth_level(self):
		return self.userAuthLevel


	def get_id(self):
		return self.userEmail


	@staticmethod
	def validate_login(password_hash, password):
		return check_password_hash(password_hash, password)



	# TO DO 
	def check_if_user_structure_is_partner(self) :
		pass

	# TO DO 
	def create_jwt_token(self):
		pass 

	# TO DO 
	def create_API_key(self):
		pass

	# TO DO 
	def update_existing_user(self):
		pass