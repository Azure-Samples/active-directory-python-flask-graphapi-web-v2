---
services: active-directory
platforms: python
author: navyasric
---

# Sign in Azure AD + MSA Users using Python-Flask Open Source Libraries

> [!NOTE]
> This sample is using a 3rd party library that has been tested for compatibility in basic scenarios with the v2.0 endpoint.  Microsoft does not provide fixes for these libraries and has not done a review of these libraries.  Issues and feature requests should be directed to the library's open-source project.  Please see this [document](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-libraries) for more information.   
> 
>

This sample demonstrates how to use Azure AD with a 3rd party Python-Flask library ([flask-oauthlib](https://github.com/lepture/flask-oauthlib)) to do oAuth 2.0 against the v2.0 endpoint.  It then makes a call to the me endpoint of the Microsoft Graph to get information about the user. 

## Steps to Run
1. Install Flask using pip if you don't already have it.  If you do, make sure to update Flask.     
    ```
    sudo pip install Flask
    ```

2. Register your Azure AD v2.0 app.  
    - Navigate to the [App Registration Portal](https://identity.microsoft.com). 
    - Go to the the `My Apps` page, click `Add an App`, and name your app.  
    - Set a platform by clicking `Add Platform`, select `Web`, and add a Redirect URI of ```http://localhost:5000/login/authorized```.
    - Click "Generate New Password' and record your Consumer Secret.  

3. Clone the code. 
    ```
    git clone https://github.com/Azure-Samples/active-directory-python-flask-graphapi-web-v2
    ```

4. In the top of v2flaskapp.py, add your Application/Client ID and Consumer Secret to the app config.

5. Set your flask environment variable and run the sample in the terminal! Navigate to `http://localhost:5000`.
    ```
    $ export FLASK_APP=v2flaskapp.py && flask run
    ```

## Questions and Issues

Please file any questions or problems with the sample as a github issue.  You can also post on StackOverflow with the tag ```azure-active-directory```.  For oAuth2.0 library issues, please see note above. 

This sample was tested with Python 2.7.10, Flask 0.11.1, and Flask-OAuthlib 0.9.3.

## Acknowledgements

The flask & django libraries are built ontop of the core python oauthlib.

[flask-oauthlib](https://github.com/lepture/flask-oauthlib)

[oauthlib](https://github.com/idan/oauthlib)

[django-oauth-toolkit](https://github.com/evonove/django-oauth-toolkit)
