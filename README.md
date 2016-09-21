# v2 Flask App 

This is a small flask app that uses the [flask-oauthlib](https://github.com/lepture/flask-oauthlib) to do oAuth2.0 against the v2 endpoint.  It displays the /me endpoint.

## Authors

Daniel Dobalian ([dadobali@microsoft.com](mailto:dadobali@microsoft.com))

## Steps to Run

Install & setup Flask if you haven't done so.  

Register an Azure AD v2 app to obtain a client id (or consumer key).  Click "Generate New Password', this will beyour consumer secret.  Then add Redirect URI's for all the routes in the app. 

Finally, set your flask path and run the flask app.  Naviagte to localhost:5000 and sign in.

## References

The flask & django libraries are built ontop of the oauthlib.

[oauthlib](https://github.com/idan/oauthlib)

[flask-oauthlib](https://github.com/lepture/flask-oauthlib)

[django-oauth-toolkit](https://github.com/evonove/django-oauth-toolkit)
