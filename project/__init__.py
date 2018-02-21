#################
#### imports ####
#################
from flask import Flask

import psycopg2
 
################
#### config ####
################
 
#app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True) #config in the instance folder is the current one
app.config.from_pyfile('config.py')

try:
    conn = psycopg2.connect(app.config['DATABASE_URI'])
except:
    print('unable to connect to the database')

####################
#### blueprints ####
####################
 
from project.main.routes import main_blueprint
from project.users.routes import users_blueprint
from project.products.routes import products_blueprint
 
# register the blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(products_blueprint)