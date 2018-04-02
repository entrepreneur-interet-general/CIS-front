
print "backend / config_vars_keep_secret.py / read "

"""
main config file --> to keep secret 
stores main secret keys and app passwords
"""

""" APP SECRET KEY """
SECRET_KEY			= "DZEFSDWCDGQdffjvhcdshcxgfdfxbwvsQQ#dzefs36421u"
WTF_CSRF_SECRET_KEY = "fgqlkshgnxrdrgebvxwdxghsbdwfvsw<eq"


""" HOST """
DOMAIN_ROOT			= "XXX.XXX.XXX.X" ### your real prod IP here
DOMAIN_PORT			= "8000"
SERVER_NAME			= "XXX.XXX.XXX.XXX:8000"  ### if True need to set SESSION_COOKIE_DOMAIN
DOMAIN_NAME			= "http://XXX.XXX.XXX.XXX:8000"
SERVER_NAME_TEST	= "False" 


# """ PORT SOCKETIO """
# PORT_EVENTLET		= "4000"


""" MONGODB """
MONGO_DBNAME	= 'cis_front'
MONGO_URI		= 'mongodb://0.0.0.0:27017/cis_front'


""" MAILING """
VALIDITY_CONFIRM	= "7"
VALIDITY_CHGPWD		= "1"

MAIL_DEFAULT_SENDER = "EMAIL_HERE@gmail.com" 
MAIL_PASSWORD       = "EMAIL_PWD" 
MAIL_SERVER         = "smtp.googlemail.com"
MAIL_USERNAME       = "EMAIL_HERE@gmail.com"


""" RECAPTCHA """ ## from https://www.google.com/recaptcha/admin#site/338490121?setup and jparis.py@gmail.com account
RECAPTCHA_SECRET_KEY = "REDO RECAPTCHA SECRET KEY"
RECAPTCHA_SITE_KEY   = "REDO RECAPTCHA SITE KEY"


""" CONFIG GOOGLE ANALYTICS / ... """
""" 
	INDEXING  : https://www.google.com/webmasters/verification/verification?hl=en&siteUrl=http://solidata.cleverapps.io/&continue=https://www.google.com/webmasters/tools/dashboard?hl%3Den%26authuser%3D3%26siteUrl%3Dhttp://solidata.cleverapps.io/%26sig%3DALjLGbMSPbWTn48JKVqv7WClemAPnPysHg&theme=wmt&authuser=3&priorities=vfile,vmeta,vdns,vanalytics,vtagmanager&tid=alternate 
	ANALYTICS : https://analytics.google.com/analytics/web/?authuser=3#management/Settings/a105171735w157018175p158556390/%3Fm.page%3DTrackingDataCollection/
"""