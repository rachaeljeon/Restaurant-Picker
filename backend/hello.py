import os
import psycopg2
from dotenv import load_dotenv
from enum import unique
import requests
from YelpAPI import get_my_key
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
