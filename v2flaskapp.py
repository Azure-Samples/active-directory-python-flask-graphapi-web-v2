from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth, OAuthException
from logging import Logger
import uuid

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

# Put your consumer key and consumer secret into a config file
# and don't check it into github!!
microsoft = oauth.remote_app(
	'microsoft',
	consumer_key='Register your app at apps.dev.microsoft.com',
	consumer_secret='Register your app at apps.dev.microsoft.com',
	request_token_params={'scope': 'offline_access User.Read'},
	base_url='https://graph.microsoft.com/v1.0/',
	request_token_url=None,
	access_token_method='POST',
	access_token_url='https://login.microsoftonline.com/common/oauth2/v2.0/token',
	authorize_url='https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
)


@app.route('/')
def index():
	if 'microsoft_token' in session: 
		return redirect(url_for('me'))
	return redirect(url_for('login'))

@app.route('/login')
def login():

	# Generate the guid to only accept initiated logins
	guid = uuid.uuid4()
	session['state'] = guid

	return microsoft.authorize(callback=url_for('authorized', _external=True), state=guid)

@app.route('/logout')
def logout():
	session.pop('microsoft_token', None)
	session.pop('state', None)
	return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
	response = microsoft.authorized_response()

	if response is None:
		return "Access Denied: Reason=%s\nError=%s" % (
			request.args['error'], 
			request.args['error_description']
		)

	# Check response for state
	if str(session['state']) != str(request.args['state']):
		raise Exception('State has been messed with, end authentication')
		
	# Okay to store this in a local variable, encrypt if it's going to client
	# machine or database. Treat as a password. 
	session['microsoft_token'] = (response['access_token'], '')

	return redirect(url_for('me'))

@app.route('/me')
def me():
	me = microsoft.get('me')
	return jsonify(me.data)

# If library is having trouble with refresh, uncomment below and implement refresh handler
# see https://github.com/lepture/flask-oauthlib/issues/160 for instructions on how to do this

# Implements refresh token logic
# @app.route('/refresh', methods=['POST'])
# def refresh():

@microsoft.tokengetter
def get_microsoft_oauth_token():
	return session.get('microsoft_token')

if __name__ == '__main__':
	app.run()
