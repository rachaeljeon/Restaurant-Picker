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

    return business_data['businesses']
    # print(business_data.keys())

    # arr = []
    # for biz in business_data['businesses']:    
    #     arr.append(biz)

    # print(business_data['businesses'])

if __name__ == '__main__':
    app.run()
