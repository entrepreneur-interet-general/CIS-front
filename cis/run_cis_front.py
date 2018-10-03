# -*- encoding: utf-8 -*-

import os
import click 

### set environment variable 
# os.environ['FLASK_CONFIGURATION'] = "default" # "testing" / "production"
### change environment var to "production" for debugging
# os.environ['FLASK_CONFIGURATION'] = "production"


# from app import app

debug = True




@click.command()
@click.option('--mode', default="default", 	nargs=1,	help="The <mode> you need to run the app : default, testing, production" )
@click.option('--host', default="None", 	nargs=1,	help="The <host> name you want the app to run on : <IP_NUMBER> " )
@click.option('--port', default="None", 	nargs=1,	help="The <port> number you want the app to run on : <PORT_NUMBER>")
def app_runner(mode, host, port) :
	"""
	app_runner

	"""

	print "= "*50
	print "= = = RERUN FLASK APP FROM APP RUNNER = = ="
	print "= "*50


	### WARNING : CLIck will treat every input as string as defaults values are string too
	print "\n=== CUSTOM CONFIG FROM CLI ===\n"
	print "=== mode : ", mode
	print "=== host : ", host
	print "=== port : ", port

	### apply / overwrites host configuration
	if mode != "default" : 
		print "=== mode : ", mode
		os.environ["FLASK_CONFIGURATION"] = str(mode)
		config_name = os.getenv('FLASK_CONFIGURATION', 'default') ### 'default' for local dev
		print "=== config_name : ", config_name

	### create app by importing app.__init__
	from app import app

	### apply / overwrites host configuration
	# app_host = app.config["DOMAIN_ROOT"]
	if host == "None" : 
		app_host 	= app.config["DOMAIN_ROOT"]
	else : 
		app_host 	= host

	### apply / overwrites port configuration
	# app_port = int(app.config["DOMAIN_PORT"])
	if port == "None" : 
		app_port 	= int(app.config["DOMAIN_PORT"])
	else : 
		app_port 	= port

	### simple flask runner
	app.run( debug=debug, host=app_host, port=app_port, threaded=True )



if __name__ == '__main__':
	""" 
	runner for the CIS front Flask app 
	- gets most of its variables at start from environment variables
	- 

	in command line just type : 
	"python run_cis_front.py"

	"""

	app_runner()

	# print "= "*50
	# print "= = = RERUN FLASK APP = = ="
	# print "= "*50

	# app_port = int(app.config["DOMAIN_PORT"])
	# app_host = app.config["DOMAIN_ROOT"]

	# # simple flask runner
	# app.run( debug=debug, host=app_host, port=app_port, threaded=True )