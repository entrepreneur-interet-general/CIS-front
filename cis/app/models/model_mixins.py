
"""
mixin classes to inject into several models later
"""

from . 	import FORM_FIELDS_TO_IGNORE, time, datetime

from .. import log_cis, pformat


class ModelMixin :


	def populate_from_form(self, form=None) : 
		"""
		retrieve form data and populate class (from .forms) 
		"""

		for f_field in form : 
			if f_field.name not in FORM_FIELDS_TO_IGNORE :
				"""
				do not save password here : 
				password needs to be hashed and should be initialized at __init__
				"""
				log_cis.debug("f_field.name : %s / f_field.data: %s ", f_field.name, f_field.data)
				self.__dict__[ f_field.name ] = f_field.data


	def populate_from_dict(self, dict_input=None) : 
		"""
		populate class from dict (as from a pymongo query)
		"""
		for k,v in dict_input.iteritems() :
			log_cis.debug("k : %s / v : %s ", k, v )
			self.__dict__[ k ] = v


	def insert_to_mongo(self, coll=None ):
		"""
		save current model as document in mongoDB, in defined collection coll
		"""
		
		# convert object to dict
		obj_as_dict = self.__dict__
		log_cis.debug("obj_as_dict : \n %s", pformat(obj_as_dict))

		# save it to collection
		coll.insert( obj_as_dict )


	def add_created_by(self, 	created_by		= None,
								created_at		= None ) :

		self.created_by 		= created_by
		self.created_at 		= created_at


	def add_modified_by(self, last_modified_by = "system") : 

		self.last_modified_by 	= last_modified_by
		self.last_modified_at 	= time.time() 		# put timestamp