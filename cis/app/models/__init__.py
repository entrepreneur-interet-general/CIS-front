# -*- encoding: utf-8 -*-


FORM_FIELDS_TO_IGNORE 	= [ "userPassword", "registerpassword", "userConfirmPassword", "csrf_token" ]
VALUES_TO_CAPITALIZE	= [ "userName", "userSurname"]

import time, datetime 

# first import mixin classes
from 	model_mixins		import *

# then import classes potentially using mixin classes 
from	model_user			import *
from	model_preregister	import *
from	model_partner		import *
