# -*- encoding: utf-8 -*-

from . 	import *
from .. import app, log_cis, pformat

log_cis.info(">>> reading _forms.form_user.py ")


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES FOR USERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


choices_data_type		= [	(u"data_company"	, u"données sur votre structure"),
							(u"data_network"	, u"données sur vos réseaux"  ),
							(u"data_activity"	, u"données sur une de vos activités"),
							(u"data_people"		, u"données sur une des personnes travaillant dans votre structure"),
						]

choices_networks		= [	(u"network_up"		, u"structures auxquelles j'adhère"),
							(u"network_flat"	, u"structures avec qui je travaille"),
							(u"network_down"	, u"structures de mon propre réseau"),
						]
						
choices_structures		= [ (u""				, u"- sélectionnez votre structure -"),

							(u""				, u"*** structures partenaires ***"  ),
							(u"apriles"			, u"Apriles"),
							(u"avise"			, u"Avise"),
							(u"cget"			, u"CGET"),
							(u"fnce"			, u"FNCE"),
							(u"fonda"			, u"La Fonda"),
							(u"cognac_jay"		, u"Fondation Cognac-Jay"),
							(u"gniac"			, u"GNIAC"),
							(u"labo_ess"		, u"Le Labo de l'ESS"),

							(u"other"			, u"*** autres structures ***"  ),
							(u"_no_"			, u"sans structure"  ),
							(u"other"			, u"autre (merci de compléter)"),
						]

choices_auth_level		= [	(u"visitor"			, u"visiteur"),
							(u"user"			, u"utilisateur"),
							(u"staff"			, u"membre du collectif"),
							(u"admin"			, u"administrateur"),
						]

choices_profile				= [	(u""				, u"- sélectionnez votre profil de métier -"),

								(u"observer"		, u"observateur.trice"),
								(u"analyst"			, u"analyste"),
								(u"helper"			, u"accompagnateur.trice"),
								(u"financer"		, u"financeur.euse"),
								(u"project_holder"	, u"porteur.euse de projet"),
								(u"citizen"			, u"citoyen.ne"),
							]

choices_structure_profile	= [	(u""				, u"- sélectionnez le profil de votre structure -"),

								(u"priv_social"		, u"association"),
								(u"priv_social"		, u"entreprise ESS ou sympathisante"),

								(u"network"			, u"tête de réseau"),
								(u"network"			, u"coopérative"),
								(u"network"			, u"mutuelle"),
								
								(u"public"			, u"structure publique"),
								(u"public"			, u"para-public"),
								
								(u"priv_commercial"	, u"fondation"),
								(u"priv_commercial"	, u"entreprise hors ESS"),
						]


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER FIELDS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


### commons infos about user 

# userName_large	= StringField	( 	u'user name', 
# 									validators = [ DataRequired(), Length(min=3, max=50) ], 
# 									render_kw={'class': 'input is-large'	, 'placeholder': u"votre prénom *"  }  
# 								)
userName		= StringField	( 	u'user name', 
									validators = [ DataRequired(), Length(min=3, max=50) ], 
									render_kw={'class': 'input'	, 'placeholder': u"votre prénom *"  }  
								)
userSurname		= StringField	( 	u'user surname' , 
									validators = [ DataRequired(), Length(min=3, max=50) ], 
									render_kw={'class': 'input'	, 'placeholder': u"votre nom *"  }  
								)
# userEmail_large	= EmailField	( 	u'user email'   , 
# 									validators = [ DataRequired(), Length(min=7, max=50) ], 
# 									render_kw={'class': 'input is-large', 'placeholder': u"votre email"  }  
# 								)
userEmail		= EmailField	( 	u'user email'   , 
									validators = [ DataRequired(), Length(min=7, max=50) ], 
									render_kw={'class': 'input', 'placeholder': u"votre email *"  }  
								)
# userPassword_large 	= PasswordField	( 	u'user password', 
# 									validators = [ DataRequired() ], 
# 									render_kw={'class': 'input is-large', 'placeholder': u"votre mot de passe"  }
# 								) 
userPassword 		= PasswordField	( 	u'user password', 
									validators = [ DataRequired() ], 
									render_kw={'class': 'input', 'placeholder': u"votre mot de passe *"  }
								) 

registerPassword 	= PasswordField ( 	u'user password',
									validators = [
										DataRequired(),
										EqualTo('userConfirmPassword', message=u"les deux mots de passe doivent être identiques"),
										Length(min=4, max=100)
									],
									render_kw={'class': 'input', 'placeholder': u"tapez votre password *"}
								)
userConfirmPassword = PasswordField ( 	u'repeat Password', 
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
											choices 	= choices_structures , 
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
										choices   	= choices_profile , 
										render_kw 	= { 'class'      : 'input select',
														'data-width' : "100%",
														'description': u"votre profil de structure"
											}
									)
userStructureProfile 	= SelectField	( 	u"le profil de votre structure", 
										validators 	= [ Optional() ],
										choices   	= choices_structure_profile , 
										render_kw 	= {   'class'      : 'input select',
														'data-width' : "100%",
														'description': u"votre profil de structure"
											}
									)
userAuthLevel			= SelectField	( 	u"votre niveau d'autorisation", 
										validators 	= [ Optional() ],
										choices 	= choices_auth_level , 
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


class PreRegisterForm( RegisterForm ) : 

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

class UserAdminInfos(UserAdminSharedInfos, UserAdminStructureInfos, UserAdminAuthLevel, UserAdminProfile, UserAdminBasics) : 
	"""
	mixin form to display a user in admin  
	"""
	pass

	# structure 		= InlineFormField( UserAdminStructureInfos )
	# shared_infos 	= InlineFormField( UserAdminSharedInfos )
	# profile 		= InlineFormField( UserAdminProfile )
	# auth_level 		= InlineFormField( UserAdminAuthLevel )

	# auth_level		= InlineFieldList(InlineFormField(UserAdminAuthLevel))



