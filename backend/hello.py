import os
import psycopg2
from dotenv import load_dotenv
from enum import unique
from tabnanny import check
import requests
from YelpAPI import get_my_business_key, get_my_category_key
from flask import Flask
from flask_cors import CORS, cross_origin

CREATE_ROOM_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_TEMPS_TABLE = """CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, 
                        date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)

GLOBAL_GET_ID = (
    """SELECT COUNT(*) FROM rooms"""
)

load_dotenv() # loads variables from .env file into environment

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)

API_KEY = get_my_business_key()
HEADERS = {
    'Authorization': 'bearer %s' % API_KEY,
    'Access-Control-Allow-Origin': '*',
    'Accept': 'application/json, text/plain, */*'
}

#-----------------------------------------------------------------------------
# BUSINESS SEARCH
# Define the endpoint
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

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

# Retrieve data from server

# @app.route('/')
# def create_room():
#     name = 'rachael'
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(GLOBAL_GET_ID)
#             # cursor.execute(INSERT_ROOM_RETURN_ID, (name, ))
#             count_id = cursor.fetchone()[0]
#     return {"total ids": count_id}, 201

@app.route('/')
def hello_world():
    #Make a request to Yelp API
    response = requests.get(url=CAT_ENDPOINT, params=CAT_PARAMS, headers=HEADERS)
    
    # Convert: JSON to dictionary
    business_data = response.json()
    arr_buz = business_data["categories"] # [{'alias': 'x', 'title': 'fast food'}, {'alias': 'x', 'title': 'fast food'}, ..., {'alias': 'x', 'title': 'fast food'}]
    
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