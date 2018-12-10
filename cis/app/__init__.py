# -*- encoding: utf-8 -*-


"""
front app du Carrefour des Innovations Sociales : 
-------------------------------------------------
version : 0.1
-------------------------------------------------
- framework back 	: flask
- landing page 		: pure html + Bulma
- logged pages 		: Vue.js ?

"""


print
print "__init__ / global imports for functions"


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### GLOBAL IMPORTS  
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  os
from    os import environ
import	time, datetime
from	datetime import timedelta
from 	datetime import date
import	json
from 	pprint import pprint, pformat
from	bson import json_util
from	bson.objectid import ObjectId
from	bson.json_util import dumps
import	itertools
import	unidecode
import	re
from	functools import wraps
# from   threading import Thread
import	urllib2
import	uuid

import inspect

# ### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# ### SET LOGGER 
# ### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from backend.config_logging import log_cis
log_cis.debug('>>> TESTING LOGGER')

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FLASK IMPORTS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask 			import Flask, g, current_app, session, request
from 	flask_wtf.csrf 	import CSRFProtect
# from	flask import jsonify, flash, render_template, url_for, make_response, request, redirect

import  socket

try : 
	host_IP = socket.gethostbyname( socket.gethostname() )
	log_cis.info( ">>> host IP : %s " , host_IP )
except: 
	log_cis.error(">>> no IP host detected")



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FLASK-ADMIN IMPORT 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
from	flask_admin 	import Admin, AdminIndexView
from 	flask_admin.model import typefmt
from 	flask_admin.model.widgets import XEditableWidget

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CRYPTO IMPORT 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  bcrypt
import	jwt



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SCHEDULER IMPORT  
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### no need for now 
# from flask_apscheduler import APScheduler
# from flask_apscheduler.auth import HTTPBasicAuth



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### MONGO DB IMPORTS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask_pymongo import PyMongo ### flask_pymongo instead of flask.ext.pymongo
# import 	pymongo
# from 	pymongo import MongoClient
# from 	pymongo import UpdateOne



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SETTINGS AT MAIN LEVEL 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### create Flask app 
app		= Flask( __name__ )

### FOR DEBUGGING PURPOSES
### LOG / PRINT HEADERS
@app.before_request
def before_request():
	
	print
	print "+ - "*25

	log_cis.debug( '/// NEW REQUEST /// ' )

	### print headers
	# log_cis.debug( '/// REQUEST HEADERS : \n %s ', request.headers )
	### NOTE BUG : 
	### SAFARI HEADERS DON'T CONTAIN COOKIE, THEREFORE NOR CSRF VALUE
	


### set environment and app variables
log_cis.debug(">>> configuring app's env vars...\n")

from .backend.config_env import * 

configure_app(app)

if config_name == "default" or config_name == "production" or config_name == "testing"  :
	log_cis.info('>>> config_name : %s \n', config_name )
	log_cis.info(	">>> ENVIRONMENT VARIABLES / to understand what the fuck is goin on ... : \n %s \n", 
					pformat({ k : v for k,v in  os.environ.iteritems() }) )
	log_cis.info(	">>> APP.CONFIG / to understand what the fucking fuck is goin on ... : \n %s \n", 
					pformat({ k : v for k,v in  app.config.iteritems() }) )
print



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN MANAGER 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from  	flask_login import 	LoginManager, login_user, logout_user, login_required, \
							current_user

### create login manager
login_manager 				= LoginManager()
login_manager.init_app(app)
login_manager.login_view 	= 'login'


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CSRF 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# deprecated --> messing with form.validate_on_submit()
# csrf = CSRFProtect(app)
# csrf.init_app(app)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### EMAILING IMPORTS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### TO DO : password forgotten 

from	flask_mail import Mail, Message

### set flask-email after config
mail 	= Mail(app)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INITIATE MONGO DB AND IMPORT MAIN CLASSES 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# settings classes : global variable for app
from 	settings 	import *
log_cis.info(">>> LIST_PARTNERS : \n %s", pformat(LIST_PARTNERS) )

# utils 
from 	utils		import *

# models :
from 	models 	import *

# set Anonymous user class
login_manager.anonymous_user = AnonymousUser

# forms classes :
from forms import * # LoginForm, UserRegisterForm, UserUpdateForm, UserHistoryAloesForm, RequestCabForm


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INITIATE MONGO DB 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# db classes and functions
from api import *

# create fields in user documents if fields doesn't exit yet
mongo_users.update_many({'verified_as_partner'	: {"$exists" : False}}, {"$set": {'verified_as_partner'	: 'no'}})
mongo_users.update_many({'created_at'			: {"$exists" : False}}, {"$set": {'created_at'			: datetime.datetime.now() }})
mongo_users.update_many({'last_modified_by'		: {"$exists" : False}}, {"$set": {'last_modified_by'	: "system" }})
mongo_users.update_many({'login_last_at'		: {"$exists" : False}}, {"$set": {'login_last_at'		: datetime.datetime.now() }})
mongo_users.update_many({'logins_total'			: {"$exists" : False}}, {"$set": {'logins_total'		: 1 }})
mongo_users.update_many({'follow_up_user'		: {"$exists" : False}}, {"$set": {'follow_up_user'		: "- suivi des échanges avec l'utilisateur -" }})

# mongo_users.update_many({'follow_up_user'		: {"$exists" : False}}, {"$set": {'follow_up_user'		: "- suivi des échanges avec l'utilisateur -" }})
mongo_users.update_many({'userNewsletter'		: {"$exists" : False}}, {"$set": {'userNewsletter'		: True }})

for user in mongo_users.find({}):
	# mod_doc = modify_doc(doc)
	user['userName']	= user['userName'].capitalize()
	user['userSurname'] = user['userSurname'].capitalize()
	mongo_users.save(user)


# create fields in feedback documents if fields doesn't exit yet
# note : files created are ignored by .gitignore
mongo_feedbacks.update_many({'created_at'			: {"$exists" : False}}, {"$set": {'created_at'			: datetime.datetime.today() }})
mongo_feedbacks.update_many({'follow_up_feedback'	: {"$exists" : False}}, {"$set": {'follow_up_feedback'	: "- suivi du message de l'utilisateur -" }})

for user in mongo_feedbacks.find({}):
	# mod_doc = modify_doc(doc)
	user['userName']	= user['userName'].capitalize()
	user['userSurname'] = user['userSurname'].capitalize()
	mongo_feedbacks.save(user)

### TEMPORARY FUNCTIONS FOR CLEANING WHILE DEVELOPPING
### WARNING : COMMENT THIS BEFORE PUSHING TO PROD
# mongo_users.update_many({}, {"$set": { "last_modified_by": "" } } )
# mongo_users.update_many({}, {"$unset": { "userCreatedAt":1 } } )
# mongo_users.update_many({}, {"$unset": { "userLastModifiedAt":1 } } )


# backup all collections when restart in ./_backups_collections
cwd = os.getcwd()
log_cis.debug('>>> BACKUP MONGO COLLECITONS : cwd : %s', cwd )

reboot_datetime = datetime.datetime.now().strftime("%Y-%m-%d-h%H-m%M-s%S")
backup_mongo_collection(mongo_users,	 cwd + "/app/_backups_collections/backup_coll_users-"+reboot_datetime +".json")
backup_mongo_collection(mongo_feedbacks, cwd + "/app/_backups_collections/backup_coll_feedbacks-"+reboot_datetime +".json")



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### IMPORT VIEWS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from . import views



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CREATE ADMIN MANAGER VIEWS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# cf : https://github.com/flask-admin/flask-admin/blob/master/examples/pymongo/app.py


admin = Admin(	app, 
				index_view=views.MyAdminIndexView(), 
				name='back office',
				# template_mode="bootstrap2"
				)

# Add views in admin interface
admin.add_view( views.UserViewAdmin( mongo_users, 		'Users' ) )
admin.add_view( views.FeedbackAdmin( mongo_feedbacks, 	'Feedbacks' ) )
admin.add_view( 
	views.ReferencedProjectCarrierFeedback(
		mongo_join_message_referenced_project_carrier, 
		u"Porteurs de projets référencés"
	) 
)
admin.add_view( 
	views.NotReferencedProjectCarrierFeedback(
		mongo_join_message_not_referenced_project_carrier,
		u"Porteurs de projets non-référencés"
	)
)
admin.add_view( views.StructuresFeedback( mongo_join_message_structures, u"Structures" ) )



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

print
log_cis.debug(">>> all imports are finished...\n")