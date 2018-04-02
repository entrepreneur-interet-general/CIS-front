# -*- encoding: utf-8 -*-


from .. import app, PyMongo, log_cis, pformat


# set as OK to run with app.context()
with app.app_context():

	mongo = PyMongo(app)

	log_cis.info(">>> starting app --- MongoDB connected")

	### access mongodb collections ###
	mongo_users		= mongo.db.users

	mongoColls = {
		"users"	: mongo_users,
	}


log_cis.debug(">>> MongoDB collections names : \n %s", pformat( mongoColls.keys() ) )
