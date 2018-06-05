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
		self.login_last_at	= datetime.datetime.now()
		self.logins_total	= 0


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


	def __init__(self, 	
						userOID			= None,
						userName		= None,
						userEmail		= None, 
						userPassword	= None,
						userAuthLevel	= "visitor",
						userRememberMe	= True,

						login_last_at	= None,
						logins_total	= 0,

						follow_up_user	= "- suivi utilisateur -",

						temp_pwd		= None,

						userFavorites	= [],

						):
		"""
		datamodel for a user in CIS_front
		- includes a UserMixin from flask-login
		- take care of keeping same field names than in forms
		"""

		log_cis.debug("creating User / userOID = %s", userOID)

		# session and auth variables

 		self.userRememberMe 		= userRememberMe

 		self.userOID 				= userOID
 		self.userEmail 				= userEmail
 		self.userAuthLevel 			= userAuthLevel
 		self.userPassword 			= userPassword
 		self.userPublicKeyAPI 		= None

		# session metrics 

		self.login_last_at			= login_last_at
		self.logins_total			= logins_total

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

		self.userNewsletter			= None 

 		self.userPartnerStructure 	= None
		self.userOtherStructure		= None
 		self.userStructureProfile 	= None
 		self.userStructureSiret 	= None


		### FOR MODERATION 

		self.verified_as_partner 	= None
		self.follow_up_user			= follow_up_user


		### PREFERENCES
		self.userFavorites			= userFavorites


	@property
	def is_admin_level(self):
		return self.userAuthLevel == "admin"

	@property
	def is_staff_level(self):
		return self.userAuthLevel in ["admin", "staff"]


	@property
	def get_public_infos(self):
		
		return { 	
					u"userOID" 				: self.userOID, 
					u"userName" 			: self.userName, 
					u"userSurname" 			: self.userSurname, 
					u"userEmail" 			: self.userEmail, 

					u"userPartnerStructure"	: self.userPartnerStructure, 
					u"userOtherStructure"	: self.userOtherStructure, 
					u"userStructureProfile" : self.userStructureProfile, 

					u"userAuthLevel" 		: self.userAuthLevel,
					u"is_authenticated" 	: self.is_authenticated
				}

	def get_auth_level(self):
		return self.userAuthLevel


	def get_id(self):
		return self.userEmail


	@staticmethod
	def validate_login(password_hash, password):
		return check_password_hash(password_hash, password)


	def setCreatedAt(self) :
		self.userCreatedAt = datetime.datetime.now()

	def setLastModifiedAt(self) :
		self.userLastModifiedAt = datetime.datetime.now()

	def check_if_user_structure_is_partner(self) :
		"""
		update self.admin_has_verified_as_partner 
		- for now : an admin has to manually check if user can be upgraded 
			from "user" to "staff"
		- TO DO : send an email to admins to alert a new partener member had created an account
		"""
		if self.userPartnerStructure in LIST_PARTNERS :
			# self.admin_has_verified_as_partner = "VERIFY"
			# self.verified_as_partner = False
			self.verified_as_partner = CHOICES_VERIFY_USER_IS_PARTNER_LIST[2]
		

	# TO DO 
	def create_jwt_token(self):
		pass 

	# TO DO 
	def create_API_key(self):
		pass


	# # TO DO  
	# def update_existing_user(self):
	# 	pass


### TO DO 
# class UserPreferences( ModelMixin ) :

# 	def __init__(self, 	userName		= None,
# 						userEmail		= None, 
# 						userPassword	= None,
# 						userPassword	= None,

# 					):
# 	"""
# 	UserPreferences for a user in CIS_front
# 	- includes a UserMixin from flask-login
# 	- take care of keeping same field names than in forms
# 	"""

# 	log_cis.debug("creating UserPreferences")