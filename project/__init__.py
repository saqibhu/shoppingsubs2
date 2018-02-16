#################
#### imports ####
#################
from flask import Flask
 
################
#### config ####
################
 
#app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

####################
#### blueprints ####
####################
 
from project.users.routes import users_blueprint
from project.products.routes import products_blueprint
 
# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(products_blueprint)