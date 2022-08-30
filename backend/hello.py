from enum import unique
from tabnanny import check
import requests
from YelpAPI import get_my_business_key, get_my_category_key
from flask import Flask
from flask_cors import CORS, cross_origin

# from backend.YelpAPI import get_my_category_key

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

API_BUSINESS_KEY = get_my_business_key()
API_CATEGORY_KEY = get_my_category_key()
BUSINESS_HEADERS = {
    'Authorization': 'bearer %s' % API_BUSINESS_KEY,
    'Access-Control-Allow-Origin': '*',
    'Accept': 'application/json, texxt/plain, */*'
}
CATEGORY_HEADERS = {
    'Authorization': 'bearer %s' % API_CATEGORY_KEY,
    'Access-Control-Allow-Origin': '*',
    'Accept': 'application/json, texxt/plain, */*'
}

#-----------------------------------------------------------------------------
# BUSINESS SEARCH
# Define the endpoint
BUZ_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
CAT_ENDPOINT = 'https://api.yelp.com/v3/categories'

# Define the parameters
BUZ_PARAMS = {
    'term': 'coffee',
    'limit': 50,
    'radius': 10000,
    'location': 'Buffalo, NY'
}

CAT_PARAMS = {
    'locale': 'en_US'
}
#-----------------------------------------------------------------------------

@app.route('/')
def hello_world():
    #Make a request to Yelp API
    response = requests.get(url=CAT_ENDPOINT, params=CAT_PARAMS, headers=CATEGORY_HEADERS)
    
    # Convert: JSON to dictionary
    business_data = response.json()
    arr_buz = business_data["categories"] # [{'alias': 'x', 'title': 'fast food'}, {'alias': 'x', 'title': 'fast food'}, ..., {'alias': 'x', 'title': 'fast food'}]
    #return arr_buz
    name_of_restaurants = []
    for cat in arr_buz: # {'alias': 'x', 'parent_aliases': 'restaurants'}
        key = 'parent_aliases'
        if key in cat:
            check_restaurant = cat[key]
            if check_restaurant == ["restaurants"]:
                if 'title' in cat:
                    title = cat['title']
                    name_of_restaurants.append(title)
    return name_of_restaurants