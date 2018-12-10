# -*- encoding: utf-8 -*-


from .. import app, PyMongo, log_cis, pformat, json, json_util


# set as OK to run with app.context()
with app.app_context():

	mongo = PyMongo(app)

	log_cis.info(">>> starting app --- MongoDB connected")

	### access mongodb collections ###
	mongo_users			= mongo.db[ app.config["MONGO_COLL_USERS"] ]
	mongo_feedbacks		= mongo.db[ app.config["MONGO_COLL_FEEDBACKS"] ]
	mongo_join_message_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_REFERENCED_PROJECT_CARRIER"] ]
	mongo_join_message_not_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_NOT_REFERENCED_PROJECT_CARRIER"] ]
	mongo_join_message_structures = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_STRUCTURES"] ]

	mongoColls = {
		# "users"	: mongo_users,
		app.config["MONGO_COLL_USERS"]			: mongo_users,
		app.config["MONGO_COLL_FEEDBACKS"]		: mongo_feedbacks,
	}


log_cis.debug(">>> MongoDB / mongoColls.keys() : \n %s", pformat( mongoColls.keys() ) )

log_cis.info(">>> MongoDB : mongo_users 		: \n %s", mongo_users  )
log_cis.info(">>> MongoDB : mongo_feedbacks 	: \n %s", mongo_feedbacks  )


def backup_mongo_collection(coll, filepath) :
	"""
	dumps all documents in collection in _backups_collections 
	"""

	cursor 		= coll.find({})
	backup_file = open(filepath, "w")
	backup_file.write('[')
	for document in cursor:
		backup_file.write(json.dumps(document,indent=4, default=json_util.default))
		backup_file.write(',')
	backup_file.write(']')



print 
