# -*- encoding: utf-8 -*-


import string
import random

from ..settings import *

# from : https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python 
def pwd_generator( size=16, chars=string.ascii_uppercase + string.digits):
	"""
	create a random password
	"""
	return ''.join(random.choice(chars) for _ in range(size))


# def get_filters_choices() : 

# 	filters_choices = [
# 						{ "domains" 	: {	
# 											"fullname"	: u"Domaines",		
# 											"choices"	: CHOICES_DOMAINS ,
# 										} 	
# 						},
# 						{ "geoloc"		: {	
# 											"fullname"	: u"Localisations",	
# 											"choices"	: [] ,
# 										} 				
# 						},
# 						{ "partners"	: {	"fullname" 	: u"Sourceurs",		
# 											"choices"	: CHOICES_PARTNERS , 
# 										}	
# 						},
# 						{ "publics"		: {	"fullname"	: u"Publics",		
# 											"choices"	: CHOICES_PUBLICS ,
# 										}	
# 						},
# 						{ "methods"		: {	
# 											"fullname"	: u"Méthodes",		
# 											"choices"	: CHOICES_METHODS , 
# 										}	
# 						},
# 					]

# 	return filters_choices