# TO DO:
# link up the small functions to the email validations

from flask import Flask, request, redirect, render_template

import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

# THIS CREATES ROUTE TO DISPLAY THE FORM

@app.route('/signup')
def display_user_signup_form():
    return render_template('main.html')

# THESE ARE FUNCTIONS FOR THE VALIDATIONS

def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def has_space(x):
    if " " not in x:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

# THIS CREATES ROUTE TO PROCESS AND VALIDATE THE FORM

@app.route("/signup", methods=['POST'])
def user_signup_complete():

    # THIS CREATES VARIABLES FROM THE FORM INPUTS

    username = request.form['username']
    password = request.form['password']
    password_validate = request.form['password_validate']
    email = request.form['email']

    # THIS CREATES EMPTY STRINGS FOR THE ERROR MESSAGES

    username_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""

    # THIS IS THE PASSWORD VALIDATION

    if not empty_val(password):
        password_error = "Password cannot be blank"
        password = ''
        password_validate = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
        password = ''
        password_validate = ''
    else:
        if " " in password:
            password_error = "Password must not contain spaces"
            password = ''
            password_validate = ''

    # THIS IS THE SECOND PASSWORD VALIDATION

    if not empty_val(password_validate):
        password_validate_error = "Password cannot be blank"
        password = ''
        password_validate = ''
    elif len(password_validate) < 3 or len(password) > 20:
        password_validate_error = "Password must be between 3 and 20 characters"
        password = ''
        password_validate = ''
    elif " " in password_validate:
            password_validate_error = "Password must not contain spaces"
            password = ''
            password_validate = ''
    else:
        if password_validate != password:
            password_validate_error = "Passwords must match"
            password = ''
            password_validate = ''

    # THIS IS THE USERNAME VALIDATION

    if not empty_val(username):
        username_error = "Username cannot be blank"
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    else:
        if " " in username:
            username_error = "Username must not contain spaces"
            password = ''
            password_validate = ''
            password_error = 'Please re-enter password'
            password_validate_error = 'Please re-enter password'

    # THIS IS THE EMAIL VALIDATION

    if not char_length(email):
        email_error = "Email must be between 3 and 20 characters"
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    elif not email_at_symbol(email):
        email_error = "Email must contain the @ symbol"
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    elif not email_at_symbol_more_than_one(email):
        email_error = "Email must contain only one @ symbol"
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    elif not email_period(email):
        email_error = "Email must contain a ."
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    elif not email_period_more_than_one(email):
        email_error = "Email must contain only one ."
        password = ''
        password_validate = ''
        password_error = 'Please re-enter password'
        password_validate_error = 'Please re-enter password'
    else:
        if " " in email:
            email_error = "Email must not contain spaces"
            password = ''
            password_validate = ''
            password_error = 'Please re-enter password'
            password_validate_error = 'Please re-enter password'

    # THIS IS THE FINAL RESULT

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)

# THIS REDIRECTS TO A WELCOME PAGE

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()