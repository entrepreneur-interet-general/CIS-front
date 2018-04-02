
import os

print
config_name = os.getenv('FLASK_CONFIGURATION', 'default') ### 'default' for local dev
print "$ config_class.py / config_name : ", config_name 

correction_env_path = {
	"development"   : "",
	"testing"       : "",
	"production"    : "",
	"default"       : ""       ### 'default' for local development
}
repath_env_vars = correction_env_path[config_name]


### set environment default variables from gitignored config_mail_recaptcha.py
try :
	
	# load secret env vars and keys
	if config_name == "default" : 
		from .config_secret_vars_example import *
	
	elif config_name == "production" : 
		from .config_secret_vars_prod import *

	os.environ["SECRET_KEY"]			= SECRET_KEY
	os.environ["WTF_CSRF_SECRET_KEY"]	= WTF_CSRF_SECRET_KEY

	os.environ["DOMAIN_NAME"]			= DOMAIN_NAME
	os.environ["DOMAIN_ROOT"]			= DOMAIN_ROOT
	os.environ["DOMAIN_PORT"]			= DOMAIN_PORT

	os.environ["SERVER_NAME"]			= SERVER_NAME
	os.environ["SERVER_NAME_TEST"]		= SERVER_NAME_TEST

	# os.environ["PORT_EVENTLET"]		= PORT_EVENTLET
	
	os.environ["RECAPTCHA_SECRET_KEY"]	= RECAPTCHA_SECRET_KEY
	os.environ["RECAPTCHA_SITE_KEY"]	= RECAPTCHA_SITE_KEY

	os.environ["VALIDITY_CONFIRM"]		= VALIDITY_CONFIRM
	os.environ["VALIDITY_CHGPWD"]		= VALIDITY_CHGPWD

	os.environ["MAIL_DEFAULT_SENDER"]	= MAIL_DEFAULT_SENDER
	os.environ["MAIL_PASSWORD"]			= MAIL_PASSWORD
	os.environ["MAIL_SERVER"]			= MAIL_SERVER
	os.environ["MAIL_USERNAME"]			= MAIL_USERNAME

	os.environ["MONGODB_DB"]			= MONGO_DBNAME
	os.environ["MONGODB_URI"]			= MONGO_URI

### except if no production env 
except : 
	pass 



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

	""" MONGODB """
	MONGO_DBNAME		=  os.getenv("MONGODB_DB")
	MONGO_URI			=  os.getenv("MONGODB_URI")

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

	""" RUNNING ENVIRONNEMENT """
	RUNNING_ENV			= os.getenv("RUNNING_ENV")



class TestingConfig(Config):
	
	TESTING = True


config = {

	"development"	: "%sapp.backend.config_.DevelopmentConfig"    %(repath_env_vars),
	"testing"		: "%sapp.backend.config_.TestingConfig"        %(repath_env_vars),
	"production"	: "%sapp.backend.config_.ProductionConfig"     %(repath_env_vars),    	
	"default"		: "app.backend.config_.DevelopmentConfig"      ### 'default' for local 
}


def configure_app(app):
	""" configure Flask app from object created above """

	print "$ config_class.py / config[config_name] : ",  config[config_name] 

	app.config.from_object( config[config_name] )
	print "$ app.config['RUNNING_ENV'] : ",   app.config["RUNNING_ENV"]
	print "$ app.config['MONGO_DBNAME'] : ",  app.config["MONGO_DBNAME"]
	print