

from . 	import FORM_FIELDS_TO_IGNORE, ModelMixin, time, datetime

from .. import log_cis, pformat


class PreRegister(ModelMixin):

	def __init__(self):
		"""
		datamodel for a Preregister data in CIS_front
		- take care of keeping same field names than in forms
		"""

		log_cis.info("creating a PreRegister class object")		

