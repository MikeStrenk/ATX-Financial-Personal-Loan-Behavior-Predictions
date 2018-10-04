from flask_wtf import FlaskForm
from wtforms import TextField, Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired


class TestForm(FlaskForm):
    first_name = TextField("firstName")
    last_name = TextField("lastName")


class LoginForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = PasswordField('lastname', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit Application')


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
