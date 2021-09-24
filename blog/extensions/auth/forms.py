import wtforms as wtf
from flask_wtf import FlaskForm


class SignInForm(FlaskForm):
    username = wtf.StringField('Username', [wtf.validators.DataRequired()])
    password = wtf.PasswordField('Password', [wtf.validators.DataRequired()])
    remember_me = wtf.BooleanField('Remember me')
    submit = wtf.SubmitField('Sign In')
