# project/recipes/routes.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, jsonify

from helpers import is_logged_in
import maindata
 
 
################
#### config ####
################
 
products_blueprint = Blueprint('products', __name__, template_folder='templates')
 
################
#### routes ####
################

@products_blueprint.route('/getproducts', methods=['POST'])
@is_logged_in
def getproducts():
    data = maindata.getProducts(request.form['searchItem'])
    return jsonify(data)
 
@products_blueprint.route('/products', methods=['GET'])
@is_logged_in
def products():
    return render_template('products.html')