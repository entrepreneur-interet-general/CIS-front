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

import time, datetime
from   datetime import timedelta
import json
import pprint
from   bson import json_util
from   bson.objectid import ObjectId
from   bson.json_util import dumps
import itertools
import unidecode
import re
from   functools import wraps
# from   threading import Thread
import urllib2
import uuid
import logging


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FLASK IMPORTS ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from    flask import Flask, g
from    flask import jsonify, flash, render_template, url_for, make_response, request, session, redirect
import  os
from    os import environ
import  socket

host_IP = socket.gethostbyname( socket.gethostname() )
print  "__init__ / host IP : " , host_IP


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CRYPTO IMPORT ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  bcrypt
import	jwt



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN MANAGER ###########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from  flask_login import LoginManager


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### EMAILING IMPORTS ########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask_mail import Mail, Message


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SCHEDULER IMPORT  #######################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### no need for now 
# from flask_apscheduler import APScheduler
# from flask_apscheduler.auth import HTTPBasicAuth



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### MONGO DB IMPORTS ########################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import 	pymongo
from 	pymongo import MongoClient
from 	pymongo import UpdateOne




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SETTINGS AT MAIN LEVEL ###################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### create Flask app 
# app			= Flask(__name__, static_path = SITE_STATIC ) ### change static directory adress to custom address for Flask
app			= Flask( __name__ ) ### change static directory adress to custom address for Flask

### set env and app variables
from .backend.config_ import * 
configure_app(app)

if config_name == "default" or config_name == "production" :

	print "__init__.py / config_name : %s" %(config_name)
	print

	print "__init__.py  / ENVIRONMENT VARIABLES / to understand what the fuck is goin on ... "
	for k, v in os.environ.iteritems() :
		print "  ", k, ":", v
	print

	print "__init__.py  / APP.CONFIG / to understand what the fucking fuck is goin on ... "
	pprint.pprint ({ k : v for k,v in  app.config.iteritems() })
	print

print


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INITIATE LOGIN MANAGER ##################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### create login manager
login_manager = LoginManager()
login_manager.init_app(app)


### set flask-email after config
mail 	= Mail(app)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### IMPORT VIEWS ############################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from . import views