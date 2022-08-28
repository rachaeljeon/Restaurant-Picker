from enum import unique
import requests
from YelpAPI import get_my_key
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

API_KEY = get_my_key()
HEADERS = {
    'Authorization': 'bearer %s' % API_KEY,
    'Access-Control-Allow-Origin': '*',
    'Accept': 'application/json, texxt/plain, */*'
}

#-----------------------------------------------------------------------------
# BUSINESS SEARCH
# Define the endpoint
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

# Define the parameters
PARAMS = {
    'term': 'coffee',
    'limit': 50,
    'radius': 10000,
    'location': 'Buffalo, NY'
}

#-----------------------------------------------------------------------------

@app.route('/')
def hello_world():
    #Make a request to Yelp API
    response = requests.get(url=ENDPOINT, params=PARAMS, headers=HEADERS)

    # Convert: JSON to dictionary
    business_data = response.json()
    arr_buz = business_data['businesses']

    arr_cat = []
    for dic in arr_buz:
        just_cat_value_shown_as_list = dic['categories'] # [{'a': 'coffe', 'title': 'dope'}]
        just_cat_as_obj = just_cat_value_shown_as_list[0] # {'a': 'coffe', 'title': 'dope'}
        just_cat_title = just_cat_as_obj['title'] # 'dope'

        if just_cat_title not in arr_cat:
            arr_cat.append(just_cat_title)
    return arr_cat
