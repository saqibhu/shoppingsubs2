# project/recipes/routes.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, jsonify, session
from helpers import is_logged_in, isProductSubscribed, getUserId
from project import conn

import psycopg2.extras
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
    if (request.method == 'POST'):
        originalData = maindata.getProducts(request.form['searchItem'])
        amendedData = []

        userId = getUserId(session['email'])

        for data in originalData:
            isSubscribed = isProductSubscribed(userId, data['id'])

            if isSubscribed:
                data['subscribed'] = 'Yes'
            else:
                data['subscribed'] = 'No'
    
            amendedData.append(data)

        data = amendedData
    else:
        data = 'no data'

    return jsonify(data)
 
@products_blueprint.route('/products', methods=['GET'])
@is_logged_in
def products():
    return render_template('products.html')

@products_blueprint.route('/subscribe', methods=['GET','POST'])
@is_logged_in
def subscribe():
    if request.method == 'POST':
        productName = request.form['name']
        productPrice = request.form['price']
        productId = request.form['id']
        productImage = request.form['image']
        productSubscribed = request.form['subscribed']

        #Get id for user account
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""select * from users where email = '%s'""" % session['email'])
        result = cur.fetchone()

        if result:
            userId = result['id']
            
            if productSubscribed == 'No':
                #Add subscription
                cur.execute("""insert into subscriptions (productid, productname, productprice, productimage, userid) values (%s, %s, %s, %s, %s)""", (productId, productName, productPrice, productImage, userId))
            elif productSubscribed == 'Yes':
                #Remove subscription
                cur.execute("""delete from subscriptions where userid = '%s' and productid = %s""", (userId, productId))
        else:
            print('Could not get user id')
    else:
        print('Method is not a post')

    conn.commit()
    cur.close()

    return render_template('products.html')