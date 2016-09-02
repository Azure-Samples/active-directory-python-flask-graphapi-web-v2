from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth, OAuthException
from logging import Logger

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)


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
	response = microsoft.authorize(callback=url_for('authorized', _external=True))

	# before returning 302 response to l.mso.com
		# Save state in cookies
		# Append state to response

	return response

@app.route('/logout')
def logout():
	session.pop('microsoft_token', None)
	return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
	try:
		response = microsoft.authorized_response()
	except OAuthException as e:
		return "OAuthException: " + str(e.data)


	if response is None:
		return "Access Denied: Reason=%s\nError=%s" % (
			request.args['error'], 
			request.args['error_description']
		)

	if isinstance(response, OAuthException):
		return 'Access Denied: %s' % response.message

	session['microsoft_token'] = (response['access_token'], '')
	return redirect(url_for('me'))

@app.route('/me')
def me():
	me = microsoft.get('me')
	return jsonify(me.data)


@microsoft.tokengetter
def get_microsoft_oauth_token():
	return session.get('microsoft_token')

if __name__ == '__main__':
	app.run()