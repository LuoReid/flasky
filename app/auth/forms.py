from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,validators
from wtforms.validators import Required,Length,Email
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
  email = EmailField('Email',validators=[validators.DataRequired(),Length(1,64), validators.Email()])
  password = PasswordField('Password',validators=[Required()])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField('Log In')