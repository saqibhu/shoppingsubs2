import requests
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f07414cab6e445e690c230b8b3539dda'
}
api = 'https://dev.tescolabs.com/grocery/products/?query=%s&offset=0&limit=3'

def getProducts(searchstring):
    response = requests.get(api % (searchstring), headers=headers)
    data = response.json()  

    return data['uk']['ghs']['products']['results']