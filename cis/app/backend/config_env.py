
import os

from .. import log_cis, pformat

config_name = os.getenv('FLASK_CONFIGURATION', 'default') ### 'default' for local dev

print
log_cis.info("$ config_name : %s", config_name)  

correction_env_path = {
	"development"   : "",
	"testing"       : "",
	"production"    : "",
	"default"       : ""       ### 'default' for local development
}
repath_env_vars = correction_env_path[config_name]


### set environment default variables from gitignored : config_secret_vars_prod.py
try :
	
	### load secret env vars and keys

	if config_name in ["default", "testing"] : 
		from .config_secret_vars_example import *
	
	elif config_name == "production" : 
		from .config_secret_vars_prod import *

	### load env vars

	os.environ["SECRET_KEY"]			= SECRET_KEY
	os.environ["WTF_CSRF_SECRET_KEY"]	= WTF_CSRF_SECRET_KEY
	os.environ["WTF_CSRF_ADMIN_KEY"]	= WTF_CSRF_ADMIN_KEY

	os.environ["JWT_SECRET_KEY"]		= JWT_SECRET_KEY

	os.environ["DOMAIN_NAME"]			= DOMAIN_NAME
	os.environ["DOMAIN_ROOT"]			= DOMAIN_ROOT
	os.environ["DOMAIN_PORT"]			= DOMAIN_PORT

	os.environ["SERVER_NAME"]			= SERVER_NAME
	os.environ["SERVER_NAME_TEST"]		= SERVER_NAME_TEST

	try : 
		os.environ["ALLOWED_HOSTS"]		= ALLOWED_HOSTS
	except :
		log_cis.info("no ALLOWED_HOSTS env var") 

	# os.environ["PORT_EVENTLET"]		= PORT_EVENTLET
	
	os.environ["RECAPTCHA_SECRET_KEY"]	= RECAPTCHA_SECRET_KEY
	os.environ["RECAPTCHA_SITE_KEY"]	= RECAPTCHA_SITE_KEY

	os.environ["VALIDITY_CONFIRM"]		= VALIDITY_CONFIRM
	os.environ["VALIDITY_CHGPWD"]		= VALIDITY_CHGPWD

	os.environ["MAIL_DEFAULT_SENDER"]	= MAIL_DEFAULT_SENDER
	os.environ["MAIL_PASSWORD"]			= MAIL_PASSWORD
	os.environ["MAIL_SERVER"]			= MAIL_SERVER
	os.environ["MAIL_USERNAME"]			= MAIL_USERNAME

	os.environ["MONGODB_URI"]				= MONGO_URI

### except if no production env 
except : 
	log_cis.error(" --- ENV VARS NOT LOADED CORRECTLY --- ") 



class Config(object):
	
	""" BASIC Config Class """

	""" GLOBAL_FLASK """
	static_dir  = '/static'
	uploads_dir = '/static/uploads'

	SITE_ROOT		= os.path.realpath(os.path.dirname(__file__))
	SITE_STATIC		= SITE_ROOT   +  static_dir
	SITE_UPLOADS	= SITE_ROOT   +  uploads_dir

	""" HOST """
	DOMAIN_NAME			=  os.getenv("DOMAIN_NAME")
	DOMAIN_ROOT			=  os.getenv("DOMAIN_ROOT")
	DOMAIN_PORT			=  os.getenv("DOMAIN_PORT")
	
	# SERVER_NAME		=  os.getenv("SERVER_NAME")
	SERVER_NAME_TEST	= os.getenv("SERVER_NAME_TEST")
	if SERVER_NAME_TEST == "True" :
		SERVER_NAME  =  os.getenv("SERVER_NAME")

	""" PORT SOCKETIO """
	# PORT_EVENTLET		= os.getenv("PORT_EVENTLET")

	""" RECAPTCHA """
	RECAPTCHA_ENABLED   = True

	""" SESSIONS """
	SECRET_KEY			= os.getenv("SECRET_KEY")

	""" FORMS """
	WTF_CSRF_ENABLED	= True
	WTF_CSRF_SECRET_KEY	= os.getenv("WTF_CSRF_SECRET_KEY")
	WTF_CSRF_ADMIN_KEY	= os.getenv("WTF_CSRF_ADMIN_KEY")

	""" JWT """
	JWT_SECRET_KEY		= os.getenv("JWT_SECRET_KEY")
	
	""" MONGODB """
	MONGO_DBNAME							= 'cis_front'
	MONGO_URI								= os.getenv("MONGODB_URI")
	MONGO_COLL_USERS						= "users"
	MONGO_COLL_FEEDBACKS					= "feedbacks"
	MONGO_COLL_JOIN_MESSAGE_REFERENCED_PROJECT_CARRIER = "join_message_referenced_project_carrier"
	MONGO_COLL_JOIN_MESSAGE_NOT_REFERENCED_PROJECT_CARRIER = "join_message_not_referenced_project_carrier"
	MONGO_COLL_JOIN_MESSAGE_STRUCTURES = "join_message_structures"

	""" MAILING """
	VALIDITY_CONFIRM	= os.getenv("VALIDITY_CONFIRM")
	VALIDITY_CHGPWD		= os.getenv("VALIDITY_CHGPWD")
	MAIL_PORT			= 465
	MAIL_USE_SSL		= True
	MAIL_USE_TLS		= False
	MAIL_DEFAULT_SENDER	= os.getenv("MAIL_DEFAULT_SENDER")
	MAIL_PASSWORD		= os.getenv("MAIL_PASSWORD")
	MAIL_SERVER			= os.getenv("MAIL_SERVER")
	MAIL_USERNAME		= os.getenv("MAIL_USERNAME")

	""" RECAPTCHA """
	RECAPTCHA_SECRET_KEY	= os.getenv("RECAPTCHA_SECRET_KEY")
	RECAPTCHA_SITE_KEY		= os.getenv("RECAPTCHA_SITE_KEY")


class DevelopmentConfig(Config):

	""" Development Config Class """
	DEBUG 				= True
 
	""" RUNNING ENVIRONNEMENT """
	RUNNING_ENV 		= "local" # local | preprod | prod



class ProductionConfig(Config):
	
	""" PRODUCTION Config Class """
	DEBUG 				= False

	ALLOWED_HOSTS		= os.getenv("ALLOWED_HOSTS")


	""" RUNNING ENVIRONNEMENT """
	RUNNING_ENV			= os.getenv("RUNNING_ENV", "production")



class TestingConfig(DevelopmentConfig, Config):
	
	DEBUG 				= True
	
	TESTING 			= True



### config dict to reroute to correct objects
config = {
	"development"	: "%sapp.backend.config_env.DevelopmentConfig"    %(repath_env_vars),
	"testing"		: "%sapp.backend.config_env.TestingConfig"        %(repath_env_vars),
	"production"	: "app.backend.config_env.ProductionConfig",     #%(repath_env_vars),    	
	"default"		: "app.backend.config_env.DevelopmentConfig"      ### 'default' for local 
}


### main function to configure app
def configure_app(app):
	""" configure Flask app from object created above """

	log_cis.info("$ config[config_name] : %s ",  config[config_name]  )

	log_cis.info("$ creating app.config from object...")
	app.config.from_object( config[config_name] )

	log_cis.info("$ app.config['RUNNING_ENV']  : %s ", app.config["RUNNING_ENV"] )
	log_cis.info("$ app.config['MONGO_DBNAME'] : %s ", app.config["MONGO_DBNAME"] ) 
	print