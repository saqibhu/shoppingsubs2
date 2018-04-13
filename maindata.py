import requests
import json

from flask import Flask
app = Flask(__name__, instance_relative_config=True) #config in the instance folder is the current one
app.config.from_pyfile('config.py')

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': app.config['SUBSCRIPTION_KEY']
}
api = 'https://dev.tescolabs.com/grocery/products/?query=%s&offset=0&limit=3'

def getProducts(searchstring):
    response = requests.get(api % (searchstring), headers=headers)
    data = response.json()  

    return data['uk']['ghs']['products']['results']