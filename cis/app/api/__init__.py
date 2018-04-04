# -*- encoding: utf-8 -*-


from .. import app, PyMongo, log_cis, pformat


# set as OK to run with app.context()
with app.app_context():

	mongo = PyMongo(app)

	log_cis.info(">>> starting app --- MongoDB connected")

	### access mongodb collections ###
	mongo_users		= mongo.db[ app.config["MONGO_COLL_USERS"] ]

	mongoColls = {
		# "users"	: mongo_users,
		app.config["MONGO_COLL_USERS"]	: mongo_users,
	}


log_cis.debug(">>> MongoDB / mongoColls.keys() : \n %s", pformat( mongoColls.keys() ) )
log_cis.debug(">>> MongoDB : mongo_users : \n %s", mongo_users  )
print 
