# -*- encoding: utf-8 -*-

from . 	import *
from .. import app, log_cis, pformat

from ..settings.app_choices import * 

log_cis.info(">>> reading _forms.form_user.py ")


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER FIELDS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


### commons infos about user 

# userName_large	= StringField	( 	u'user name', 
# 									validators = [ DataRequired(), Length(min=3, max=50) ], 
# 									render_kw={'class': 'input is-large'	, 'placeholder': u"votre prénom *"  }  
# 								)
userName		= StringField	( 	u'prénom', 
									validators = [ DataRequired(), Length(min=3, max=50) ], 
									render_kw={'class': 'input'	, 'placeholder': u"votre prénom *"  }  
								)
userSurname		= StringField	( 	u'nom' , 
									validators = [ DataRequired(), Length(min=3, max=50) ], 
									render_kw={'class': 'input'	, 'placeholder': u"votre nom *"  }  
								)
# userEmail_large	= EmailField	( 	u'user email'   , 
# 									validators = [ DataRequired(), Length(min=7, max=50) ], 
# 									render_kw={'class': 'input is-large', 'placeholder': u"votre email"  }  
# 								)
userEmail		= EmailField	( 	u'email'   , 
									validators = [ DataRequired(), Length(min=7, max=50) ], 
									render_kw={'class': 'input', 'placeholder': u"votre email *"  }  
								)
# userPassword_large 	= PasswordField	( 	u'user password', 
# 									validators = [ DataRequired() ], 
# 									render_kw={'class': 'input is-large', 'placeholder': u"votre mot de passe"  }
# 								) 
userPassword 		= PasswordField	( 	u'password', 
										validators = [ DataRequired() ], 
										render_kw={'class': 'input', 'placeholder': u"votre mot de passe *"  }
									) 

registerPassword 	= PasswordField ( 	u'password',
										validators = [
											DataRequired(),
											EqualTo('userConfirmPassword', message=u"les deux mots de passe doivent être identiques"),
											Length(min=4, max=100)
										],
										render_kw={'class': 'input', 'placeholder': u"tapez votre password *"}
									)
userConfirmPassword = PasswordField ( 	u'répéter le password', 
										render_kw={'class': 'input', 'placeholder': u"répétez votre mot de passe *" } 
									)

userRememberMe 		= BooleanField  ( 	u'se souvenir de moi', 
										default=False, 	
										render_kw={'class': 'is-checkradio is-black is-normal'	, 'checked':'' } 
									)


### shared data's infos about user's structure

userHaveProjects  			= BooleanField  ( 	u'J’ai des projets à valoriser'	, 
												default=False, 	
												render_kw={'class': 'is-checkradio has-background-color is-white is-normal'	 } 
											)
userHaveProjects_strong  	= BooleanField  ( 	u'<strong>J’ai des projets à valoriser</strong>'	, 
												default=False, 	
												render_kw={'class': 'is-checkradio has-background-color is-white is-normal'	 } 
											)
userJoinCollective  		= BooleanField  ( 	u'J’aimerais être partenaire du projet', 
												default=False, 	
												render_kw={'class': 'is-checkradio has-background-color is-white is-normal'	 } 
											)
userJoinCollective_strong  	= BooleanField  ( 	u'<strong>J’aimerais être partenaire du projet</strong>', 
												default=False, 	
												render_kw={'class': 'is-checkradio has-background-color is-white is-normal'	 } 
											)
userMessage					= TextAreaField	(  	u'Message', 					
												render_kw={'class' : 'textarea' , 'rows':'3', 'placeholder' : 'votre message, vos suggestions...' }
											)

### specific infos about user's structure

userStructureSiret		= IntegerField  ( 	u'le numéro de siret de votre structure',
											validators = [ Optional() ],
											render_kw={'class': 'input', 
											'placeholder':u"le numéro de SIRET de votre structure"  }  
										)
userPartnerStructure	= SelectField	( 	u'sélectionner votre structure', 
											validators 	= [ Optional() ],
											choices 	= CHOICES_STRUCTURES , 
											default   	= 0 ,
											render_kw 	= {	'class'      : 'input select',
															'data-width' : "100%",
															'description': u'votre structure'
												}
										)
userOtherStructure		= StringField	(	u'le nom de votre structure' , 
											validators = [ Optional(), Length(min=0, max=50) ], 
											render_kw={'class': 'input', 'placeholder': u"le nom de votre structure"  }  
										)


### user preferences / auth level

userProfile 			= SelectField	( 	u"votre profil métier", 
											validators 	= [ Optional() ],
											choices   	= CHOICES_PROFILES , 
											render_kw 	= { 'class'      : 'input select',
															'data-width' : "100%",
															'description': u"votre profil de structure"
												}
										)
userStructureProfile 	= SelectField	( 	u"le profil de votre structure", 
											validators 	= [ Optional() ],
											choices   	= CHOICES_STRUCTURE_PROFILE , 
											render_kw 	= {   'class'      : 'input select',
															'data-width' : "100%",
															'description': u"votre profil de structure"
												}
										)
userAuthLevel			= SelectField	( 	u"votre niveau d'autorisation", 
											validators 	= [ Optional() ],
											choices 	= CHOICES_AUTH_LEVEL , 
											default   	= "user",
											render_kw 	= {	'class'      : 'input select',
															'data-width' : "100%",
															'description': u"votre niveau d'authorization"
												}
										)
userPublicKeyAPI		= StringField	(	u'user Public Key for the API' , 
											validators 	= [ Optional(), Length(min=0, max=50) ], 
											render_kw	= {'class': 'input', 'placeholder': u"votre token"  }  
										)

temp_pwd				= StringField	(	u'temporary password for user' , 
											validators 	= [ Optional(), Length(min=0, max=50) ], 
											render_kw	= {'class': 'input', 'placeholder': u"votre token"  }  
										)




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER FORMS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


### USER STRUCTURE FOR MIXINS

class UserBasics(FlaskForm) :
	userEmail 			= userEmail
	userPassword 		= userPassword

class UserID(FlaskForm) :
	userName 			= userName
	userSurname 		= userSurname

class UserProfile(FlaskForm) :
	userProfile			= userProfile

class UserStructureInfos(FlaskForm) :
	userStructureSiret		= userStructureSiret
	userStructureProfile 	= userStructureProfile
	userPartnerStructure	= userPartnerStructure
	userOtherStructure 		= userOtherStructure

class UserSharedInfos(FlaskForm) :
	userHaveProjects 	= userHaveProjects
	userJoinCollective	= userJoinCollective
	userMessage			= userMessage



### USER FORMS

class LoginForm( UserBasics ):

	userEmail			= userEmail
	userPassword 		= userPassword
	userRememberMe		= userRememberMe


class RegisterForm( UserSharedInfos, UserStructureInfos, UserProfile, UserID):
	
	### user infos
	userEmail		= userEmail

	### user password
	registerPassword 	= registerPassword
	userConfirmPassword = userConfirmPassword

	### optionnal infos
	userRememberMe 	= userRememberMe


class PreRegisterForm( UserSharedInfos, UserStructureInfos, UserProfile, UserID):

	### user infos
	userEmail		= userEmail

	userHaveProjects 	= userHaveProjects_strong
	userJoinCollective	= userJoinCollective_strong


class PwdForgotForm( FlaskForm ):

	userName		= userName
	userEmail		= userEmail


class NewPwdForm( FlaskForm ):

	userPassword 		= registerPassword
	userConfirmPassword	= userConfirmPassword






### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ADMIN USER FORMS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py   




class UserAdminBasics(form.Form) : 
	
	userName 			= userName
	userSurname 		= userSurname
	userEmail 			= userEmail
	# userPassword 		= userPassword
	temp_pwd			= temp_pwd	

class UserAdminStructureInfos(form.Form) : 

	userStructureSiret		= userStructureSiret
	userStructureProfile 	= userStructureProfile
	userPartnerStructure 	= userPartnerStructure
	userOtherStructure 		= userOtherStructure

class UserAdminSharedInfos(form.Form) : 

	userHaveProjects 	= userHaveProjects
	userJoinCollective	= userJoinCollective
	userMessage			= userMessage

class UserAdminProfile(form.Form) : 

	userProfile			= userProfile

class UserAdminAuthLevel(form.Form) : 

	userAuthLevel 		= userAuthLevel
	userPublicKeyAPI 	= userPublicKeyAPI


### USER ADMIN 

class UserAdminInfos(UserAdminSharedInfos, UserAdminStructureInfos, UserAdminAuthLevel, UserAdminProfile, UserAdminBasics) : 
	"""
	mixin form to display a user in admin  
	"""
	pass

class MessagesFromLandingAdmin (UserAdminSharedInfos, UserAdminBasics) :
	"""
	mixin form to display messages sent from landing
	"""
	userOtherStructure 		= userOtherStructure



