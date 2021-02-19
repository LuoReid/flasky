from flask_wtf import Form,FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,validators
from wtforms.validators import DataRequired,Required,Length,Email,Regexp,EqualTo
from wtforms.fields.html5 import EmailField
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
  email = EmailField('Email',validators=[validators.DataRequired(),Length(1,64), validators.Email()])
  password = PasswordField('Password',validators=[Required()])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField('Log In')

class RegistrationForm(Form):
  email = EmailField('Email',validators=[validators.DataRequired(),Length(1,64), validators.Email()])
  username = StringField('Username',validators=[validators.DataRequired(),\
    Length(1,64),Regexp('^[A-Za-z][A-za-z0-9_.]*$',0,'Usernames must have only letters,numbers,dots or underscores')])
  password = PasswordField('Password',validators=[Required(),EqualTo('password2',message='Passwords must match.')])
  password2 = PasswordField('Confirm password',validators=[Required()])
  submit = SubmitField('Register')

  def validate_email(self,field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError('Email already registered.')
  
  def validate_username(self,field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError('Username already in use.')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')
