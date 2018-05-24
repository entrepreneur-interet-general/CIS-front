# -*- encoding: utf-8 -*-

from . 	import *
from .. import app, log_cis, pformat, datetime

from ..settings.app_choices import * 

log_cis.info(">>> reading _forms.form_user.py ")


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER FIELDS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### custom hidden fields
userOID 			= HiddenField("userOID")
userEmailHidden 	= HiddenField("userEmailHidden")


### commons infos about user 

created_at 			= DateField 	( 	u"crée le", 
										format="%Y-%m-%d @ %H:%M:%S",
										default=datetime.datetime.now, ## Now it will call it everytime.
										# validators=[ DataRequired() ]
									)
last_modified_at 	= DateField 	( 	u"modifié le",
										format="%Y-%m-%d @ %H:%M:%S",
										default=datetime.datetime.now,
									)

# userName_large	= StringField	( 	u'user name', 
# 									validators = [ DataRequired(), Length(min=3, max=50) ], 
# 									render_kw={'class': 'input is-large'	, 'placeholder': u"votre prénom *"  }  
# 								)
userName		= StringField	( 	u"prénom", 
									validators = [ 
										DataRequired(			message=u"vous devez rentrer un prénom"), 
										Length(min=3, max=50,	message=u"vous devez rentrer un prénom d'au moins 3 caractères ")
									], 
									render_kw={'class': 'input'	, 'placeholder': u"votre prénom *"  }  
								)
userSurname		= StringField	( 	u"nom" , 
									validators = [ 
										DataRequired(			message=u"vous devez rentrer un nom pour valider"), 
										Length(min=3, max=50, 	message=u"vous devez rentrer un nom d'au moins 3 caractères ") ], 
									render_kw={'class': 'input'	, 'placeholder': u"votre nom *"  }  
								)
# userEmail_large	= EmailField	( 	u'user email'   , 
# 									validators = [ DataRequired(), Length(min=7, max=50) ], 
# 									render_kw={'class': 'input is-large', 'placeholder': u"votre email"  }  
# 								)
userEmail		= EmailField	( 	u"email"   , 
									validators = [ 
										DataRequired(			message=u"email invalide"), 
										Length(min=7, max=50) 
									], 
									render_kw={'class': 'input', 'placeholder': u"votre email *"  }  
								)



# userPassword_large 	= PasswordField	( 	u'user password', 
# 									validators = [ DataRequired() ], 
# 									render_kw={'class': 'input is-large', 'placeholder': u"votre mot de passe"  }
# 								) 
userPassword 		= PasswordField	( 	u"votre mot de passe", 
										validators = [ 
											DataRequired( 		message=u"vous devez rentrer un mot de passe" ),
											Length(min=4, 		message=u"vous devez rentrer un mot de passe plus long") 
											], 
										render_kw={'class': 'input', 'placeholder': u"votre mot de passe *"  }
									)
registerPassword 	= PasswordField ( 	u"votre mot de passe",
										validators = [
											DataRequired(			message=u"vous devez rentrer un mot de passe" ),
											EqualTo(				'userConfirmPassword', 
																	message=u"les deux mots de passe doivent être identiques"),
											Length(min=4, max=100, 	message=u"vous devez rentrer un mot de passe")
										],
										render_kw={'class': 'input', 'placeholder': u"tapez votre mot de passe *"}
									)
oldPassword 		= PasswordField	( 	u"votre ancien mot de passe", 
										validators = [ 
											DataRequired( 		message=u"vous devez rentrer votre mot de passe actuel" ),
											Length(min=4, 		message=u"vous devez rentrer un mot de passe plus long") 
											], 
										render_kw={'class': 'input', 'placeholder': u"votre mot de passe"  }
									) 
newPassword 		= PasswordField ( 	u"votre nouveau mot de passe",
										validators = [
											DataRequired(			message=u"vous devez rentrer un nouveau mot de passe" ),
											EqualTo(				'userConfirmPassword', 
																	message=u"les deux mots de passe doivent être identiques"),
											Length(min=4, max=100, 	message=u"vous devez rentrer un mot de passe")
										],
										render_kw={'class': 'input', 'placeholder': u"tapez votre mot de passe"}
									)
userConfirmPassword = PasswordField ( 	u"répéter le mot de passe", 
										render_kw={'class': 'input', 'placeholder': u"répétez votre mot de passe" } 
									)





userRememberMe 		= BooleanField  ( 	u"se souvenir de moi", 
										default=False, 	
										render_kw={'class': 'is-checkradio is-black is-normal'	, 'checked':'' } 
									)

userAcceptCGU 		= BooleanField  ( 	u"j'accepte les conditions générales d'utilisation", 
										validators = [ 
											DataRequired(	message=u"merci de bien cocher la case") 
											] ,
										default 	= False, 	
										render_kw = {'class': 'is-checkradio is-black is-normal'	, 'checked':'' } 
									)
userNewsletter 		= BooleanField  ( 	u"je souhaite recevoir la newsletter du Carrefour des innovations sociales", 
										default 	= False, 	
										render_kw = {'class': 'is-checkradio is-black is-normal' },
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
											default		= 0 ,
											render_kw 	= {	'class'      : 'input select',
															'data-width' : "100%",
															'description': u'votre structure'
												}
										)
userOtherStructure		= StringField	(	u'le nom de votre structure' , 
											validators = [ Optional(), Length(min=0, max=75) ], 
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
															'description': u"votre niveau d'authorisation"
												}
										)
userPublicKeyAPI		= StringField	(	u'user Public Key for the API' , 
											validators 	= [ Optional(), Length(min=0, max=75) ], 
											render_kw	= {'class': 'input', 'placeholder': u"votre token"  }  
										)

temp_pwd				= StringField	(	u'temporary password for user' , 
											validators 	= [ Optional(), Length(min=0, max=75) ], 
											render_kw	= {'class': 'input', 'placeholder': u"votre token"  }  
										)


### JUST FOR ADMIN AND MODERATION 

verified_as_partner		= SelectField	( 	u"un.e admin a vérifié que l'utilisateur peut passer en staff", 
											validators 	= [ Optional() ],
											default		= "no",
											choices   	= CHOICES_VERIFY_USER_IS_PARTNER , 
											render_kw 	= { 'class'      : 'input select',
															'data-width' : "100%",
															'description': u"utilisateur s'est enregistré comme faisant partie d'une structure partenaire"
												}
										)

follow_up_user			= TextAreaField	(  	u'Suivi utilisateur', 					
												render_kw={'class' : 'textarea' , 'rows':'3', 'placeholder' : u"suivi des échanges avec l'utilisateur" }
											)

follow_up_feedback		= TextAreaField	(  	u'Suivi du message', 					
												render_kw={'class' : 'textarea' , 'rows':'3', 'placeholder' : u"suivi du message de l'utilisateur" }
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
	userNewsletter	= userNewsletter
	userRememberMe 	= userRememberMe
	userAcceptCGU 	= userAcceptCGU

class UserParametersForm( UserSharedInfos, UserStructureInfos, UserProfile, UserID):
	
	### user infos
	userOID				= userOID
	userEmail			= userEmail

	### optionnal infos
	userNewsletter		= userNewsletter

class UserNewPassword (FlaskForm) : 

	### user infos
	userOID				= userOID
	# userEmailHidden			= userEmailHidden
	
	### user password
	oldPassword 		= oldPassword
	newPassword 		= newPassword
	userConfirmPassword = userConfirmPassword

class PreRegisterForm( UserSharedInfos, UserStructureInfos, UserProfile, UserID):

	### user infos
	userEmail		= userEmail

	userHaveProjects 	= userHaveProjects_strong
	userJoinCollective	= userJoinCollective_strong



### TO IMPLEMENT WITH FLAKS-MAIL

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

	# created_at			= created_at

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
	verified_as_partner = verified_as_partner
	# last_modified_at	= last_modified_at
	follow_up_user		= follow_up_user

class MessagesFromLandingAdmin (UserAdminSharedInfos, UserAdminBasics) :
	"""
	mixin form to display messages sent from landing
	"""
	userOtherStructure 		= userOtherStructure
	follow_up_user			= follow_up_user


