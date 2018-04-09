# -*- encoding: utf-8 -*-


import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app import app


if __name__ == '__main__':
	""" 
	runner for the CIS front Flask app 
	- gets most of its variables at start from environment variables
	- 

	in command line just type : 
	"python run_cis_front.py"

	"""

	# set environment variable to set config later in backend.config_env.py
	os.environ['FLASK_CONFIGURATION'] = "production"

	print "= "*25
	print "= = = WSGI / RERUN FLASK APP = = ="
	print "= "*25

	# simple flask runner
	app.run( )