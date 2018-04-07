# -*- encoding: utf-8 -*-

from . 	import *
from .. import log_cis, pformat

log_cis.info(" >>> reading _forms.form_user.py ")


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES FOR USERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


choices_data_type		= [
							(u"data_company"	, u"données sur votre structure"),
							(u"data_network"	, u"données sur vos réseaux"  ),
							(u"data_activity"	, u"données sur une de vos activités"),
							(u"data_people"		, u"données sur une des personnes travaillant dans votre structure"),
						]

choices_networks		= [
							(u"network_up"		, u"structures auxquelles j'adhère"),
							(u"network_flat"	, u"structures avec qui je travaille"),
							(u"network_down"	, u"structures de mon propre réseau"),
						]
						
choices_subscriptions	= [
							(u""				, u"- sélectionnez le profil de votre structure -"),
							# (u"open_data"		, u"open data"  ),
							(u"priv_social"		, u"association"),
							(u"priv_social"		, u"entreprise ESS ou sympathisante"),
							(u"network"			, u"tête de réseau"),
							(u"network"			, u"accompagnateur"),
							(u"network"			, u"coopérative"),
							(u"network"			, u"mutuelle"),
							(u"public"			, u"structure publique"),
							(u"public"			, u"para-public"),
							(u"priv_commercial"	, u"fondation"),
							(u"priv_commercial"	, u"entreprise hors ESS"),
						]

choices_structures		= [
							(u""				, u"- sélectionnez votre structure -"),
							# (u"open_data"       , u"open data"  ),
							(u"apriles"			, u"Apriles"),
							(u"avise"			, u"Avise"),
							(u"cget"			, u"CGET"),
							(u"cognac_jay"		, u"Fondation Cognac-Jay"),
							(u"fnce"			, u"FNCE"),
							(u"fonda"			, u"La Fonda"),
							(u"gniac"			, u"GNIAC"),
							(u"labo_ess"		, u"Le Labo de l'ESS"),

							(u"other"			, u"- autre structure -"),

						]

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER FORMS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


class LoginForm(FlaskForm):

	userEmail		= EmailField	( 	u'user email'   , 
										validators = [ DataRequired(), Length(min=7, max=50) ], 
										render_kw={'class': 'input is-large', 'placeholder': u'votre email'  }  
									)
	userPassword 	= PasswordField	( 	u'user password', 
										validators = [ DataRequired() ], 
										render_kw={'class': 'input is-large', 'placeholder': u"votre mot de passe"  }  
									)
	rememberMe  	= BooleanField  ( 	u'se souvenir de moi', 
										default=False, 	
										render_kw={'class': 'is-checkradio is-black is-normal'	, 'checked':'' } 
									)


class RegisterForm(FlaskForm):
	
	### user infos

	userName		= StringField	( 	u'user name', 
										validators = [ DataRequired(), Length(min=3, max=50) ], 
										render_kw={'class': 'input'	, 'placeholder': u'votre prénom *'  }  
									)
	userSurname		= StringField	( 	u'user surname' , 
										validators = [ DataRequired(), Length(min=3, max=50) ], 
										render_kw={'class': 'input'	, 'placeholder': u'votre nom *'  }  
									)
	userEmail       = EmailField	( 	u'user email', 
										validators = [ DataRequired(), Length(min=7, max=50) ], 
										render_kw={'class': 'input'	, 'placeholder': u'votre email *'  }  
									)
	
	### user password

	userPassword    = PasswordField ( 	u'user password',
										[
											DataRequired(),
											EqualTo('confirmPassword', message=u'les deux mots de passe doivent être identiques'),
											Length(min=4, max=100)
										],
										render_kw={'class': 'input', 'placeholder': u'tapez votre password *'}
									)
	confirmPassword = PasswordField ( 	u'repeat Password', 
										render_kw={'class': 'input', 'placeholder': u'répétez votre mot de passe *' } 
										)



	### optionnal infos

	rememberMe  	= BooleanField  ( 	u'se souvenir de moi', 
										default=False, 	
										render_kw={'class': 'is-checkradio has-background-color is-black is-normal'	, 'checked':'' } 
									)

	userSiret		= IntegerField  ( 	u'user siret',
										render_kw={'class': 'input', 
										'placeholder':u'le numéro de SIRET de votre structure'  }  
									)
	userProfile		= SelectField   ( 	u'select profile', 
										choices   = choices_subscriptions , 
										# default   = "priv_social",
										render_kw = {   'class'      : 'input select',
														'data-width' : "100%",
														'description': u'votre profil de structure'
											}
									)
	userStructure	= SelectField	( 	u'select structure', 
										choices = choices_structures , 
										# default   = "other",
										render_kw = {   'class'      : 'input select',
														'data-width' : "100%",
														'description': u'votre structure'
											}
									)
	userOtherStructure	= StringField   (	u'user structure' , 
											validators = [ Length(min=3, max=50) ], 
											render_kw={'class': 'input', 'placeholder': u'le nom de votre structure'  }  
										)



class PreRegisterForm(RegisterForm) : 

	userHaveProjects  	= BooleanField  ( 	u'<strong>J’ai des projets à valoriser</strong>'	, 
											default=False, 	
											render_kw={'class': 'is-checkradio has-background-color is-white is-normal'	 } 
										)
	userJoinCollective  = BooleanField  ( 	u'<strong>J’aimerais être partenaire du projet</strong>', 
											default=False, 	
											render_kw={'class': 'is-checkradio has-background-color is-white is-normal'	 } 
										)

	userMessage 		= TextAreaField(  	u'Message', 					
											render_kw={'class' : 'textarea' , 'rows':'3', 'placeholder' : 'Votre message, vos suggestions... *' }
										)







class PwdForgotForm(FlaskForm):

	userName	= StringField	(	'user name', 
									validators = [ DataRequired(), Length(min=3, max=50) ], 
									render_kw={'class': 'input is-large', 'placeholder':u'votre prénom'  }
								)
	userEmail	= EmailField	(	'pwdforgot email', 
									validators = [ DataRequired(), Length(min=7, max=50) ],
									render_kw={'class': 'input is-large', 'placeholder':u'votre email'  }  
								)


class NewPwdForm(FlaskForm):

	userPassword	=	PasswordField	( 	'user password',
											[
												DataRequired(),
												EqualTo('confirmPassword', message=u'les deux mots de passe doivent être identiques'),
												Length(min=4, max=100)
											],
											render_kw={'class': 'input is-large', 'placeholder': u'tapez votre password'}
										)
	confirmPassword	=	PasswordField 	(	'repeat Password', 
											render_kw={'class': 'input is-large', 'placeholder':u'répétez votre mot de passe' } 
										)