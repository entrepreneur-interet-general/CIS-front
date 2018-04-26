# -*- encoding: utf-8 -*-

import os

os.environ['FLASK_CONFIGURATION'] = "default" # "testing" / "production"

### for debugging
os.environ['FLASK_CONFIGURATION'] = "production"

from app import app

debug = True



if __name__ == '__main__':
	""" 
	runner for the CIS front Flask app 
	- gets most of its variables at start from environment variables
	- 

	in command line just type : 
	"python run_cis_front.py"

	"""

	print "= "*50
	print "= = = RERUN FLASK APP = = ="
	print "= "*50

	app_port = int(app.config["DOMAIN_PORT"])
	app_host = app.config["DOMAIN_ROOT"]

	# simple flask runner
	app.run( debug=debug, host=app_host, port=app_port, threaded=True )