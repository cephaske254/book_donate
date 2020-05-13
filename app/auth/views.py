from . import auth
from flask import render_template,redirect,flash
from .forms import RegisterForm,LoginForm

@auth.route('/register')
def register():
    title= 'Register'
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/register.html', title=title,form=form)

@auth.route('/login')
def login():
    title= 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html', title=title,form=form)