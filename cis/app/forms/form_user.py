# -*- encoding: utf-8 -*-

from . import *
from .. import log_cis, pformat

log_cis.info(" >>> reading _forms.form_user.py ")


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES FOR USERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


choices_data_type       = [
							(u"data_company"    , u"données sur votre structure"),
							(u"data_network"    , u"données sur vos réseaux"  ),
							(u"data_activity"   , u"données sur une de vos activités"),
							(u"data_people"     , u"données sur une des personnes travaillant dans votre structure"),
						]

choices_networks        = [
							(u"network_up"      , u"structures auxquelles j'adhère"),
							(u"network_flat"    , u"structures avec qui je travaille"),
							(u"network_down"    , u"structures de mon propre réseau"),
						]
						
choices_subscriptions    = [
							(u"open_data"       , u"open data"  ),
							(u"priv_social"     , u"association"),
							(u"priv_social"     , u"entreprise ESS ou sympathisante"),
							(u"network"         , u"tête de réseau"),
							(u"network"         , u"coopérative"),
							(u"network"         , u"mutuelle"),
							(u"public"          , u"public"),
							(u"public"          , u"para-public"),
							(u"priv_commercial" , u"fondation"),
							(u"priv_commercial" , u"entreprise hors ESS"),
						]


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER FORMS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


class LoginForm(FlaskForm):
	userEmail       = EmailField    ( 'user email'   , validators = [ DataRequired(), Length(min=7, max=50) ], render_kw={'class': '', 'placeholder':u'votre email'  }  )
	userPassword = PasswordField ( 'user password', validators = [ DataRequired() ], render_kw={'class': '', 'placeholder':u"votre mot de passe"  }  )
	#remember_me  = BooleanField  ( 'remember_me', default=False )


class UserRegisterForm(FlaskForm):
	userName        = StringField   ( 'user name'    , validators = [ DataRequired(), Length(min=3, max=50) ], render_kw={'class': '', 'placeholder':u'votre prénom'  }  )
	userSurname     = StringField   ( 'user surname' , validators = [ DataRequired(), Length(min=3, max=50) ], render_kw={'class': '', 'placeholder':u'votre nom'  }  )
	userSiret       = IntegerField  ( 'user siret'   ,                                                         render_kw={'class': '', 'placeholder':u'votre numéro de SIRET'  }  )

	userEmail       = EmailField    ( 'user email'   , validators = [ DataRequired(), Length(min=7, max=50) ], render_kw={'class': '', 'placeholder':u'votre email'  }  )
	userPassword    = PasswordField ( 'user password',
		[
		DataRequired(),
		EqualTo('confirmPassword', message=u'les deux mots de passe doivent être identiques'),
		Length(min=4, max=100)
		],
		render_kw={'class': '', 'placeholder': u'tapez votre password'}
	)
	confirmPassword = PasswordField ('repeat Password', render_kw={'class': '', 'placeholder':u'répétez votre mot de passe' } )
	#remember_me     = BooleanField  ( 'remember_me', default=False )

	userProfile     = SelectField   ( 'select profile', choices = choices_subscriptions , default="priv_social",
														render_kw = {   'class': '',
																		'data-width' : "100%"
														 }
									)

class PwdForgotForm(FlaskForm):
	userName     = StringField   ( 'user name'         , validators = [ DataRequired(), Length(min=3, max=50) ], render_kw={'class': '', 'placeholder':u'votre prénom'  }  )
	userEmail    = EmailField    ( 'pwdforgot email'   , validators = [ DataRequired(), Length(min=7, max=50) ], render_kw={'class': '', 'placeholder':u'votre email'  }  )


class NewPwdForm(FlaskForm):
	userPassword    = PasswordField ( 'user password',
		[
		DataRequired(),
		EqualTo('confirmPassword', message=u'les deux mots de passe doivent être identiques'),
		Length(min=4, max=100)
		],
		render_kw={'class': '', 'placeholder': u'tapez votre password'}
	)
	confirmPassword = PasswordField ('repeat Password', render_kw={'class': '', 'placeholder':u'répétez votre mot de passe' } )