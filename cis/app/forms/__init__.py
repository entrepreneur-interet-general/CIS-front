# -*- encoding: utf-8 -*-


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ALLOWED EXTENSIONS FOR UPLOADED FILES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

ALLOWED_DATAFILES  = set([ 'csv', 'xls' ])
ALLOWED_IMAGES     = set([ 'png', 'jpg', 'jpeg', 'gif' ])
# ALLOWED_EXTENSIONS = set([ 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xls' ])
ALLOWED_EXTENSIONS = ALLOWED_IMAGES.union(ALLOWED_DATAFILES)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### IMPORT SPECIFIC MODULES FOR forms._init__.py
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###



#from flask_wtf import Form		### flask_wtf instead of flask.ext.wtf
from 	flask_wtf				import 	FlaskForm, RecaptchaField    ### FlaskWTFDeprecationWarning: "flask_wtf.Form" has been renamed to "FlaskForm" and will be removed in 1.0.
from 	flask_wtf.file 			import 	FileField, FileRequired, FileAllowed

from 	wtforms 				import 	validators, form, fields

### import field classes
from 	wtforms					import 	StringField, BooleanField, TextAreaField, IntegerField, \
 										PasswordField, SubmitField, HiddenField, widgets #, Form
from 	wtforms.fields.html5	import 	URLField, EmailField
from 	wtforms.fields.core 	import 	SelectField, SelectMultipleField, RadioField, DateTimeField, DateField

from 	wtforms.validators 		import 	DataRequired, Length, EqualTo, URL, Email, Optional, NumberRange

from 	flask_admin.model				import BaseModelView
from 	flask_admin.form 				import Select2Widget, SecureForm
from 	flask_admin.contrib.pymongo 	import ModelView, filters
from 	flask_admin.model.fields 		import InlineFormField, InlineFieldList

# from flask.ext.admin.contrib.pymongo.filters.BasePyMongoFilter import *


			
										  
### import forms
from 	form_user 				import *