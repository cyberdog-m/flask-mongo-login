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

class Order(FlaskForm):
    orderId = StringField('orderId')
    title = StringField('Title')
    customerName = StringField('Customer Name')
    particulars = StringField('Particulars')
    delivaryDate = DateField('Delivary Date')
    details = StringField('Details')
    orderStatus = StringField('Order Status')
    estimateAmount = StringField('Estimate Amount')
    advanceAmount = StringField('Advance Amount')

class TestForm(FlaskForm):
    item = StringField('item', validators=[DataRequired()])
    level = StringField('level')
    submit = SubmitField('Submit')