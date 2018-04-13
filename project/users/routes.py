# project/users/routes.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, flash, redirect, url_for, session

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import psycopg2.extras

from project import conn
from helpers import is_logged_in
 
################
#### config ####
################
 
users_blueprint = Blueprint('users', __name__, template_folder='templates')

################
#### classes ###
################

class RegisterForm(Form):
    name = StringField('Fullname', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')
 
################
#### routes ####
################

@users_blueprint.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""insert into users (name, email, password) values (%s, %s, %s)""", (name, email, password))
        conn.commit()
        cur.close()

        flash('You are now registered', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
 
@users_blueprint.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Get form fields
        email = request.form['email']
        password_candidate = request.form['password']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""select * from users where email = '%s'""" % email)
        result = cur.fetchone()

        if result:
            password = result['password']

            #Compare password
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['name'] = result['name']
                session['email'] = result['email']

                flash('You are now logged in', 'success')
                return redirect(url_for('products.products'))
            else:
                error = 'Invalid password'
                return render_template('login.html', error = error)

            #Close connection
            cur.close()
        else:
            error = 'Email address not found'
            cur.close()
            return render_template('login.html', error = error)
    return render_template('login.html')

@users_blueprint.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('.login'))