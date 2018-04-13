from flask import flash, redirect, url_for, session
from functools import wraps
from project import conn
import psycopg2
import psycopg2.extras

################
## functions ###
################

#Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login', 'danger')
            return redirect(url_for('users.login'))
    return wrap

def getUserId(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""select * from users where email = '%s'""" % email)
    result = cur.fetchone()
    if result:
        return result['id']
    else:
        return 'No user id'

def isProductSubscribed(userid, productid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""select * from subscriptions where userid = '%s' and productid ='%s'""" % (userid, productid))
    subscriptions = cur.fetchone()

    if subscriptions:
        return True
    else:
        return False