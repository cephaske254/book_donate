from flask_login import current_user,login_required, login_user,logout_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import Required, Email,EqualTo, ValidationError
from .. models import User

class RegisterForm(FlaskForm):
    first_name = StringField('First Name',validators=[Required()])
    last_name = StringField('Last Name',validators=[Required()])
    username = StringField('Userame',validators=[Required()])
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    confirm_password = PasswordField('Confirm Password',validators=[Required(), EqualTo('password',message='Passwords Not Equal!')])
    account_type = SelectField('Account Type', choices=['donor','beneficiary','admin'],validators=[Required()])
    agree = BooleanField('Agree to T&Cs',validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            ValidationError('Email already registered!')

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            ValidationError('Username Taken!')
    
class LoginForm(FlaskForm):
    username = StringField('Userame',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    loggen_in = BooleanField('Keep me logged in',validators=[Required()])
    submit = SubmitField('Login')