import requests
from YelpAPI import get_my_key
from flask import Flask

app = Flask(__name__)

API_KEY = get_my_key()
HEADERS = {
    'Authorization': 'bearer %s' % API_KEY
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



# from yelp.client import Client
# MY_API_KEY = "67sg5N_QqZzu3UdqCX8U5rqGbvBEBXVYu-jokMRznOO97vrlfJxSqZJUKJ_Ae_GPTWKoMM0V0W3Z00bH6IybQX4AyaBGVeHS9xMf3RF0n-udN6d7U0XwjXahHjv0YHYx" #  Replace this with your real API key

# client = Client(MY_API_KEY)

# business_response = client.business.get_by_id('yelp-san-francisco')
# print(business_response)

#-----------------------------------------------------------------------------

@app.route('/')
def hello_world():
    #Make a request to Yelp API
    response = requests.get(url=ENDPOINT, params=PARAMS, headers=HEADERS)

    # Convert: JSON to dictionary
    business_data = response.json()

    print(business_data.keys())

    for biz in business_data['businesses']:
        print(biz['name'])

    return biz['name']

if __name__ == '__main__':
    app.run()
