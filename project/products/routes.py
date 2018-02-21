# project/recipes/routes.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, jsonify

import maindata
 
 
################
#### config ####
################
 
products_blueprint = Blueprint('products', __name__, template_folder='templates')
 
 
################
#### routes ####
################

@products_blueprint.route('/getproducts', methods=['POST'])
def getproducts():
    data = maindata.getProducts(request.form['searchItem'])
    return jsonify(data)
 
@products_blueprint.route('/products', methods=['GET','POST'])
def products():
        return render_template('products.html')