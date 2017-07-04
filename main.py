from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

user_signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>User Sign-up</h1>
    <!--  form action needs to match the url you want it to go to after submit -->
    <form action="/user-signup-complete" method='POST'>
        <label>Username
            <input name="username" type="text" value='{username}' />
        </label>
        <p class="error">{username_error}</p>
        <label>Password
            <input name="password" type="text" value='{password}' />
        </label>
        <p class="error">{password_error}</p>
        <label>Password Validate
            <input name="password_validate" type="text" value='{password_validate}' />
        </label>
        <p class="error">{password_validate_error}</p>
        <label>E-mail (optional)
            <input name="email_validate" type="text" value='{email}' />
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
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

@app.route("/user-signup-complete", methods=['POST'])
def user_signup_complete():

    username = request.form['username']
    # password = request.form['password']
    # password_validate = request.form['password_validate']
    # email = request.form['email']

    username_error = ""
    # password_error = ""
    # password_validate_error = ""
    # email_error = ""

    if not empty_val(username):
        username_error = "Username cannot be blank"
    
    #if not empty_val(password):
        #password_error = "Password cannot be blank"

    #if not empty_val(password_validate):
        #password_validate_error = "Second password cannot be blank"

    #if not username_error and not password_error and not password_validate_error:
    if not username_error:
        return 'Success'
    else:
        return 'Error'

    # returns success message with username
    #return '<h1>Welcome, ' + username + '</h1>'

app.run()