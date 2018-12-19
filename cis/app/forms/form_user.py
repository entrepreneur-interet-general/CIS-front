# -*- encoding: utf-8 -*-

from . 	import *
from .. import app, log_cis, pformat, datetime

from ..settings.app_choices import * 

log_cis.info(">>> reading _forms.form_user.py ")

class MultiCheckboxField(SelectMultipleField):
	
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()


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
									render_kw={'class': 'input'}  
								)
userSurname		= StringField	( 	u"nom" , 
									validators = [ 
										DataRequired(			message=u"vous devez rentrer un nom pour valider"), 
										Length(min=3, max=50, 	message=u"vous devez rentrer un nom d'au moins 3 caractères ") ], 
									render_kw={'class': 'input'}  
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
									render_kw={'class': 'input'}  
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

FEEDBACK_TOPIC_TADATA = u'La suite logicielle tadata'
FEEDBACK_TOPIC_CIS = u'Le projet Carrefour des innovations sociales'
FEEDBACK_TOPIC_BUG = u'Un bug repéré sur le site'
FEEDBACK_TOPIC_PROPOSAL = u'Une suggestion d’amélioration'
FEEDBACK_TOPIC_OTHER = u'Un autre sujet'

userFeedbackTopic			= SelectField(		u'Sujet du message', 
												choices=[
													(FEEDBACK_TOPIC_TADATA, FEEDBACK_TOPIC_TADATA), 
													(FEEDBACK_TOPIC_CIS, FEEDBACK_TOPIC_CIS), 
													(FEEDBACK_TOPIC_BUG, FEEDBACK_TOPIC_BUG), 
													(FEEDBACK_TOPIC_PROPOSAL, FEEDBACK_TOPIC_PROPOSAL), 
													(FEEDBACK_TOPIC_OTHER, FEEDBACK_TOPIC_OTHER), 
												],
												render_kw={'id': 'feedback-topic'}
										)


userMessage					= TextAreaField	(  	u'Message', 					
												render_kw={'class' : 'textarea' , 'rows':'5'}
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
											validators = [ Optional(), Length(min=0, max=100) ], 
											render_kw={'class': 'input'}  
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

# Join us fields

structureWebsite		= StringField	(	u'site de la structure' , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
										)

personName				= StringField	(	u'nom de la personne' , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
										)

personEmail				= EmailField	( 	u"email", 
											validators = [ 
												DataRequired(message=u"email invalide"), 
												Length(min=1, max=1000) 
											], 
											render_kw={'class': 'input'}  
										)

personRole				= StringField	( 	u"role", 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
										)

projectName 			= StringField	(	u'nom du projet' , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
										)

address					= TextAreaField	(  	u'Adresse', 					
											render_kw={'class' : 'textarea' , 'rows':'3'}
										)

PROJECT_ACTION_AREA_NATIONAL = u'nationale'
PROJECT_ACTION_AREA_LOCAL = u'local'

projectActionArea		= MultiCheckboxField (	u"Périmètre d'action", 
										choices=[
											(PROJECT_ACTION_AREA_NATIONAL, PROJECT_ACTION_AREA_NATIONAL), 
											(PROJECT_ACTION_AREA_LOCAL, PROJECT_ACTION_AREA_LOCAL)
										]
									)

projectActionAreaLocalDetails	= StringField	(	u"Périmètre d'action locale détails" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
									)

PROJECT_CATEGORY_LIFE_ENV = u"Cadre de vie"
PROJECT_CATEGORY_SUST_DEV = u"Développement durable"
PROJECT_CATEGORY_ECO_DEV = u"Développement économique"
PROJECT_CATEGORY_HABITAT = u"Habitat"
PROJECT_CATEGORY_INCLUSION = u"Inclusion"
PROJECT_CATEGORY_SOCIAL_NET = u"Lien social"
PROJECT_CATEGORY_HEALTH_SPORT = u"Santé, Sport"
PROJECT_CATEGORY_EMPLOYMENT = u"Travail"

projectCategories 				= MultiCheckboxField(	u'Catégories', 
														choices=[
															(PROJECT_CATEGORY_LIFE_ENV, PROJECT_CATEGORY_LIFE_ENV),
															(PROJECT_CATEGORY_SUST_DEV, PROJECT_CATEGORY_SUST_DEV),
															(PROJECT_CATEGORY_ECO_DEV, PROJECT_CATEGORY_ECO_DEV),
															(PROJECT_CATEGORY_HABITAT, PROJECT_CATEGORY_HABITAT),
															(PROJECT_CATEGORY_INCLUSION, PROJECT_CATEGORY_INCLUSION),
															(PROJECT_CATEGORY_SOCIAL_NET, PROJECT_CATEGORY_SOCIAL_NET),
															(PROJECT_CATEGORY_HEALTH_SPORT, PROJECT_CATEGORY_HEALTH_SPORT), 
															(PROJECT_CATEGORY_EMPLOYMENT, PROJECT_CATEGORY_EMPLOYMENT)
														]
													)

projectCategoriesOther			= StringField	(	u"Autres catégories" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
									)

PROJECT_AUDIENCE_YOUTH = u"Jeunesse"
PROJECT_AUDIENCE_HANDICAP = u"Handicap"
PROJECT_AUDIENCE_ELDERLY = u"Senior"
PROJECT_AUDIENCE_OTHER = u"Autre, précisez"

projectAudiences				= MultiCheckboxField(	u'Catégories', 
														choices=[
															(PROJECT_AUDIENCE_YOUTH, PROJECT_AUDIENCE_YOUTH),
															(PROJECT_AUDIENCE_HANDICAP, PROJECT_AUDIENCE_HANDICAP),
															(PROJECT_AUDIENCE_ELDERLY, PROJECT_AUDIENCE_ELDERLY),
															(PROJECT_AUDIENCE_OTHER, PROJECT_AUDIENCE_OTHER)
														]
													)

projectAudiencesOther			= StringField	(	u"Autres publics" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
									)

projectStartYear				= StringField	(	u"Année de création" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
									)

PROJECT_STAGE_IDEA = u"Idéation"
PROJECT_STAGE_DEV = u"Développement"
PROJECT_STAGE_BOOTSTRAP = u"Amorçage"
PROJECT_STAGE_SPREAD = u"Essaimage"

projectStage					= MultiCheckboxField(	u'Catégories', 
														choices=[
															(PROJECT_STAGE_IDEA, PROJECT_STAGE_IDEA),
															(PROJECT_STAGE_DEV, PROJECT_STAGE_DEV),
															(PROJECT_STAGE_BOOTSTRAP, PROJECT_STAGE_BOOTSTRAP),
															(PROJECT_STAGE_SPREAD, PROJECT_STAGE_SPREAD)
														]
													)


projectDescription				= TextAreaField	(  	u'Description', 					
											render_kw={'class' : 'textarea' , 'rows':'5'}
										)

projectInnovation				= TextAreaField	(  	u'Innovation', 					
											render_kw={'class' : 'textarea' , 'rows':'5'}
										)

projectFundingAndPartners		= TextAreaField	(  	u'projectFundingAndPartners', 					
											render_kw={'class' : 'textarea' , 'rows':'5'}
										)

projectRewards					= StringField	(	u"Récompenses" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
									)

structureReasonToJoin			= TextAreaField	(  	u'Raison de rejoindre', 					
											render_kw={'class' : 'textarea' , 'rows':'5'}
										)


STRUCTURE_LISTS_REWARD_WINNERS = u"Je liste les lauréats de mes appels à projets"
STRUCTURE_LISTS_HELPED = u"Je liste les projets que j'accompagne"
STRUCTURE_LISTS_HIGHLIGHT = u"Je liste des projets que je cherche à valoriser"
STRUCTURE_LISTS_OTHER = u"Autre, précisez :"


structureListHow				= MultiCheckboxField(	u'Projets listés', 
														choices=[
															(STRUCTURE_LISTS_REWARD_WINNERS, STRUCTURE_LISTS_REWARD_WINNERS),
															(STRUCTURE_LISTS_HELPED, STRUCTURE_LISTS_HELPED),
															(STRUCTURE_LISTS_HIGHLIGHT, STRUCTURE_LISTS_HIGHLIGHT),
															(STRUCTURE_LISTS_OTHER, STRUCTURE_LISTS_OTHER)
														]
													)

structureListHowOther			= StringField	(	u"Projets listés (autres)" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
											)

STRUCTURE_PROJECTS_COUNT_0_15 = u"Entre 0 et 15"
STRUCTURE_PROJECTS_COUNT_15_50 = u"Entre 15 et 50"
STRUCTURE_PROJECTS_COUNT_50_200 = u"Entre 15 et 50"
STRUCTURE_PROJECTS_COUNT_MORE_THAN_200 = u"Plus de 200"

structureProjectsToShareCount	= RadioField('Label', 
												choices=[
													(STRUCTURE_PROJECTS_COUNT_0_15, STRUCTURE_PROJECTS_COUNT_0_15),
													(STRUCTURE_PROJECTS_COUNT_15_50, STRUCTURE_PROJECTS_COUNT_15_50),
													(STRUCTURE_PROJECTS_COUNT_50_200, STRUCTURE_PROJECTS_COUNT_50_200),
													(STRUCTURE_PROJECTS_COUNT_MORE_THAN_200, STRUCTURE_PROJECTS_COUNT_MORE_THAN_200)
												])

STRUCTURE_PROJECTS_INFOS_TITRE = u"Le titre du projet"
STRUCTURE_PROJECTS_INFOS_CARRIER_NAME = u"Le nom du porteur de projet"
STRUCTURE_PROJECTS_INFOS_PICTURE = u"Une photo"
STRUCTURE_PROJECTS_INFOS_LEGAL_STRUCTURE = u"La structure juridique"
STRUCTURE_PROJECTS_INFOS_DESC = u"Une description du projet"
STRUCTURE_PROJECTS_INFOS_CARRIER_EMAIL = u"Le contact du porteur de projet"
STRUCTURE_PROJECTS_INFOS_LOCALISATION = u"La localisation du projet"


structureProjectsToShareInfos = MultiCheckboxField(
	'Infos disponibles', 
	choices=[
		(STRUCTURE_PROJECTS_INFOS_TITRE, STRUCTURE_PROJECTS_INFOS_TITRE),
		(STRUCTURE_PROJECTS_INFOS_CARRIER_NAME, STRUCTURE_PROJECTS_INFOS_CARRIER_NAME),
		(STRUCTURE_PROJECTS_INFOS_PICTURE, STRUCTURE_PROJECTS_INFOS_PICTURE),
		(STRUCTURE_PROJECTS_INFOS_LEGAL_STRUCTURE, STRUCTURE_PROJECTS_INFOS_LEGAL_STRUCTURE),
		(STRUCTURE_PROJECTS_INFOS_DESC, STRUCTURE_PROJECTS_INFOS_DESC),
		(STRUCTURE_PROJECTS_INFOS_CARRIER_EMAIL, STRUCTURE_PROJECTS_INFOS_CARRIER_EMAIL),
		(STRUCTURE_PROJECTS_INFOS_LOCALISATION, STRUCTURE_PROJECTS_INFOS_LOCALISATION)
	]
)

STRUCTURE_PROJECTS_FORMAT_WEBSITE = u"Un site internet"
STRUCTURE_PROJECTS_FORMAT_EXCEL = u"Un tableau excel"
STRUCTURE_PROJECTS_FORMAT_PDF = u"Un fichier PDF"
STRUCTURE_PROJECTS_FORMAT_API = u"Une API"
STRUCTURE_PROJECTS_FORMAT_MAP = u"Une cartographie en ligne"
STRUCTURE_PROJECTS_FORMAT_WORD_DOC = u"Un fichier Word"
STRUCTURE_PROJECTS_FORMAT_DATABASE = u"Une base de données"

structureProjectsToShareFormat 	= MultiCheckboxField(
	'Formats disponibles', 
	choices=[
		(STRUCTURE_PROJECTS_FORMAT_WEBSITE, STRUCTURE_PROJECTS_FORMAT_WEBSITE),
		(STRUCTURE_PROJECTS_FORMAT_EXCEL, STRUCTURE_PROJECTS_FORMAT_EXCEL),
		(STRUCTURE_PROJECTS_FORMAT_PDF, STRUCTURE_PROJECTS_FORMAT_PDF),
		(STRUCTURE_PROJECTS_FORMAT_API, STRUCTURE_PROJECTS_FORMAT_API),
		(STRUCTURE_PROJECTS_FORMAT_MAP, STRUCTURE_PROJECTS_FORMAT_MAP),
		(STRUCTURE_PROJECTS_FORMAT_WORD_DOC, STRUCTURE_PROJECTS_FORMAT_WORD_DOC),
		(STRUCTURE_PROJECTS_FORMAT_DATABASE, STRUCTURE_PROJECTS_FORMAT_DATABASE)
	]
)

structureProjectsToShareWebsite			= StringField	(	u"Site des projets partagés" , 
											validators = [ Optional(), Length(min=1, max=1000) ], 
											render_kw={'class': 'input'}  
											)

STRUCTURE_INTEREST_ANALYSIS = u"Analyse et transmission des innovations sociales"
STRUCTURE_INTEREST_FRIEND = u"Développement du Carrefour des innovations sociales dans les territoires"
STRUCTURE_INTEREST_COLLECTIVE_ACTION_FORMS = u"Compréhension des nouvelles formes d’action collective"


structureInterests 	= MultiCheckboxField(
	'Intérêts', 
	choices=[
		(STRUCTURE_INTEREST_ANALYSIS, STRUCTURE_INTEREST_ANALYSIS),
		(STRUCTURE_INTEREST_FRIEND, STRUCTURE_INTEREST_FRIEND),
		(STRUCTURE_INTEREST_COLLECTIVE_ACTION_FORMS, STRUCTURE_INTEREST_COLLECTIVE_ACTION_FORMS)
	]
)


###
# The following field is meant to be a honeypot field added hidden to forms
# If it is filed, it means a bot filed the form and the message is spam

antiSpamField	= StringField	(	u"Middle name" , 
								validators = [ Optional() ], 
								render_kw={'class': 'input'}  
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

### Feedback forms

class FeedbackForm(UserID):

	### user infos
	userEmail			= userEmail
	userOtherStructure 	= userOtherStructure
	userFeedbackTopic   = userFeedbackTopic
	userMessage			= userMessage
	userMiddlename		= antiSpamField # hidden field used as spam honeypot

class ReferencedProjectCarrierForm(FlaskForm):
	partnerStructureName = userOtherStructure
	partnerStructureWebsite = structureWebsite
	partnerStructureContactName = personName
	partnerStructureContactEmail = personEmail
	message = userMessage
	userMiddlename		= antiSpamField # hidden field used as spam honeypot

class NotReferencedProjectCarrierForm(FlaskForm):
	projectName = projectName
	projectStructureName = userOtherStructure
	projectContactName = personName
	projectContactEmail = personEmail
	projectAddress = address
	projectActionArea = projectActionArea
	projectActionAreaLocalDetails = projectActionAreaLocalDetails
	projectCategories = projectCategories
	projectCategoriesOther = projectCategoriesOther
	projectAudiences = projectAudiences
	projectAudiencesOther = projectAudiencesOther
	projectStartYear = projectStartYear
	projectStage = projectStage
	projectDescription = projectDescription
	projectInnovation = projectInnovation
	projectFundingAndPartners = projectFundingAndPartners
	projectRewards = projectRewards
	projectWebsite = structureWebsite
	projectAttachment = FileField()
	userMiddlename		= antiSpamField # hidden field used as spam honeypot


class StructureFormCommons(FlaskForm):
	structureName = userOtherStructure
	structureWebsite = structureWebsite
	structureContactName = personName
	structureContactRole = personRole
	structureContactEmail = personEmail
	structureReasonToJoin = structureReasonToJoin
	userMiddlename		= antiSpamField # hidden field used as spam honeypot


class StructureWithProjectsForm(StructureFormCommons):
	structureListHow = structureListHow
	structureListHowOther = structureListHowOther
	structureProjectsToShareCount = structureProjectsToShareCount
	structureProjectsToShareInfos = structureProjectsToShareInfos
	structureProjectsToShareFormat = structureProjectsToShareFormat
	structureProjectsToShareWebsite = structureProjectsToShareWebsite
	structureProjectsToShareAttachment = FileField()

class StructureNoProjectsForm(StructureFormCommons):
	structureInterests = structureInterests


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


