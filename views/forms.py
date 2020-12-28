from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True})
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')

class Signup(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={'autofocus': True})
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    signup = SubmitField('Sign Up')

class Reset(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'autofocus': True})
    reset = SubmitField('Reset Password')