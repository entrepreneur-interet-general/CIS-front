# -*- encoding: utf-8 -*-

### import all from app.__init__
from . import *
# from app import app


########################################################################################
# Access token ### from prettyprinted youtube channel
def token_required(f):
	@wraps(f)
	def decorated( *args, **kwargs ):

		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return jsonify({'message' : 'Token is missing!'}), 401

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			# current_user = User.query.filter_by(public_id=data['public_id']).first()

		except:
			return jsonify({'message' : 'Token is invalid!'}), 401

		return f(current_user, *args, **kwargs)

	return decorated

	
@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():

	time_now	= datetime.datetime.utcnow()

	### FORMS FROM WTF

	### set language

	### check token from session["public_id"] 
	try :
		current_session_uid = session["public_id"]
		# Check_tokens_user ( current_session_uid, lang_set )
	except : 
		current_session_uid = None
		

	return render_template( "index.html",

							title = "carrefour des innovations sociales"

							)