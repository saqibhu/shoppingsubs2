# project/recipes/routes.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint
 
 
################
#### config ####
################
 
products_blueprint = Blueprint('products', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@products_blueprint.route('/')
def index():
    return render_template('index.html')