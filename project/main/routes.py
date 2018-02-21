# project/recipes/routes.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint
 
 
################
#### config ####
################
 
main_blueprint = Blueprint('main', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@main_blueprint.route('/')
def index():
    return render_template('index.html')