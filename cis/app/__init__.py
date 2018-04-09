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
### GLOBAL IMPORTS  #########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  os
from    os import environ
import	time, datetime
from	datetime import timedelta
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


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SET LOGGER ##############################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from backend.config_logging import log_cis
log_cis.debug('TESTING LOGGER')

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FLASK IMPORTS ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask 			import Flask, g, current_app, session, request
from 	flask_wtf.csrf 	import CSRFProtect
# from	flask import jsonify, flash, render_template, url_for, make_response, request, redirect

import  socket

try : 
	host_IP = socket.gethostbyname( socket.gethostname() )
	log_cis.info( "host IP : %s " , host_IP )
except: 
	log_cis.error("no IP host detected")



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FLASK-ADMIN IMPORT ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
from	flask_admin 	import Admin, AdminIndexView


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CRYPTO IMPORT ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  bcrypt
import	jwt



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SCHEDULER IMPORT  #######################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### no need for now 
# from flask_apscheduler import APScheduler
# from flask_apscheduler.auth import HTTPBasicAuth



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### MONGO DB IMPORTS ########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask_pymongo import PyMongo ### flask_pymongo instead of flask.ext.pymongo
# import 	pymongo
# from 	pymongo import MongoClient
# from 	pymongo import UpdateOne



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SETTINGS AT MAIN LEVEL ###################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### create Flask app 
app		= Flask( __name__ )

### FOR DEBUGGING PURPOSES
@app.before_request
def before_request():
	
	print
	print "+ - "*25

	### print headers
	log_cis.debug( 'REQUEST HEADERS : \n %s ', request.headers )
	### NOTE BUG : 
	### SAFARI HEADERS DON'T CONTAIN COOKIE, THEREFORE NOR CSRF VALUE
	

### set environment and app variables
log_cis.debug("configuring app's env vars...\n")

from .backend.config_env import * 

configure_app(app)

if config_name == "default" or config_name == "production" :

	log_cis.info('config_name : %s', config_name )
	print

	log_cis.debug(	"ENVIRONMENT VARIABLES / to understand what the fuck is goin on ... : \n %s", 
					pformat({ k : v for k,v in  os.environ.iteritems() }) )
	print

	log_cis.debug(	"APP.CONFIG / to understand what the fucking fuck is goin on ... : \n %s", 
					pformat({ k : v for k,v in  app.config.iteritems() }) )
	print

print



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN MANAGER ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from  	flask_login import 	LoginManager, login_user, logout_user, login_required, \
							current_user

### create login manager
login_manager 				= LoginManager()
login_manager.init_app(app)
login_manager.login_view 	= 'login'


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CSRF ####################################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# deprecated --> messing with form.validate_on_submit()
# csrf = CSRFProtect(app)
# csrf.init_app(app)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### EMAILING IMPORTS ########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask_mail import Mail, Message

### set flask-email after config
mail 	= Mail(app)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INITIATE MONGO DB AND IMPORT MAIN CLASSES ###############################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# settings classes : global variable for app
from settings import *

# models :
from models import *
login_manager.anonymous_user = AnonymousUser

# forms classes :
from forms import * # LoginForm, UserRegisterForm, UserUpdateForm, UserHistoryAloesForm, RequestCabForm

# db classes and functions
from api import *



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### IMPORT VIEWS ############################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from . import views



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CREATE ADMIN MANAGER VIEWS ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# cf : https://github.com/flask-admin/flask-admin/blob/master/examples/pymongo/app.py


admin = Admin(app, index_view=views.MyAdminIndexView(), name='admin interface for CIS')

# Add views
admin.add_view( views.UserViewAdmin( mongo_users, 'Users' ) )






### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

print
log_cis.debug("all imports are finished...\n")