# project/users/routes.py
 
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, flash, redirect, url_for

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

from project import conn
import psycopg2.extras
 
################
#### config ####
################
 
users_blueprint = Blueprint('users', __name__, template_folder='templates')

#Classes
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')
 
 
################
#### routes ####
################
 
@users_blueprint.route('/login')
def login():
    return render_template('login.html')

@users_blueprint.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #sql bit
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""insert into users (name, email, password) values (%s, %s, %s)""", (name, email, password))
        conn.commit()
        cur.close()

        flash('You are now registered', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)