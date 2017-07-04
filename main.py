# TO DO:
# link up the small functions to the email validations

from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

user_signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>User Sign-up</h1>
    <!--  form action needs to match the url you want it to go to after submit -->
    <form action="/" method='POST'>
        <label>Username
            <input name="username" type="text" value='{username}' />
        </label>
        <p class="error">{username_error}</p>
        <label>Password
            <input name="password" type="password" value='{password}' />
        </label>
        <p class="error">{password_error}</p>
        <label>Password Validate
            <input name="password_validate" type="password" value='{password_validate}' />
        </label>
        <p class="error">{password_validate_error}</p>
        <label>E-mail (optional)
            <input name="email" type="text" value='{email}' />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Submit" />
    </form>
    """


@app.route('/')
def display_user_signup_form():
    return user_signup_form.format(username='', username_error='',
        password='', password_error='', password_validate='', password_validate_error='', email='', email_error='', )

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

@app.route("/", methods=['POST'])
def user_signup_complete():

    username = request.form['username']
    password = request.form['password']
    password_validate = request.form['password_validate']
    email = request.form['email']

    username_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""

    # THIS IS THE USERNAME VALIDATION

    if not empty_val(username):
        username_error = "Username cannot be blank"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
    else:
        if " " in username:
            username_error = "Username must not contain spaces"

    # THIS IS THE PASSWORD VALIDATION

    if not empty_val(password):
        password_error = "Password cannot be blank"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
    else:
        if " " in password:
            password_error = "Password must not contain spaces"

    # THIS IS THE SECOND PASSWORD VALIDATION

    if not empty_val(password_validate):
        password_validate_error = "Password cannot be blank"
    elif len(password_validate) < 3 or len(password) > 20:
        password_validate_error = "Password must be between 3 and 20 characters"
    elif " " in password_validate:
            password_validate_error = "Password must not contain spaces"
    else:
        if password_validate != password:
            password_validate_error = "Passwords must match"

    # THIS IS THE EMAIL VALIDATION

    if not char_length(email):
        email_error = "Email must be between 3 and 20 characters"
    elif not email_at_symbol(email):
        email_error = "Email must contain the @ symbol"
    elif not email_at_symbol_more_than_one(email):
        email_error = "Email must contain only one @ symbol"
    elif not email_period(email):
        email_error = "Email must contain a ."
    elif not email_period_more_than_one(email):
        email_error = "Email must contain only one ."
    else:
        if " " in email:
            email_error = "Email must not contain spaces"

    # THIS IS THE FINAL RESULT

    if not username_error and not password_error and not password_validate_error and not email_error:
        return 'Success'
        #return '<h1>Welcome, ' + username + '</h1>'
    else:
        return user_signup_form.format(username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)

app.run()