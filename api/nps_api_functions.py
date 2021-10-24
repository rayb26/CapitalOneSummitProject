import requests
from bs4 import BeautifulSoup
import urllib.request

api_key = '&api_key=6uJcmYK3Buc4KNEaeKcbzh7PRwjD1bN7zJX2Maxo'


def find_park_from_keyword(keyword):
    park_list = []
    park_urls = []
    park_code_list = []

    api_request_link = 'https://developer.nps.gov/api/v1/activities/parks?q={}&limit=1000{}'.format(keyword, api_key)
    request = requests.get(api_request_link).json()
    for data in range(len(request['data'][0]['parks'])):
        park_list.append(request['data'][0]['parks'][data]['fullName'])
        park_urls.append(request['data'][0]['parks'][data]['url'])
        park_code_list.append(request['data'][0]['parks'][data]['parkCode'])

    return {

        "park_name": park_list,
        "park_urls": park_urls,
        "park_codes": park_code_list
    }


def get_coordinates(park_code):
    api_request_link = 'https://developer.nps.gov/api/v1/parks?parkCode={}{}'.format(park_code, api_key)
    request = requests.get(api_request_link).json()

    return {
        "longitude": request['data'][0]['longitude'],
        "latitude": request['data'][0]['latitude']
    }


# def grab_webcam_metadata(park_code):
#     api_request_link = 'https://developer.nps.gov/api/v1/webcams?q={}{}'.format(park_code, api_key)
#     request = requests.get(api_request_link).json()
#     print(str(request['data'][2]['images'][0]['url']))
#

def get_park_profile(park_code):
    api_request_link = 'https://developer.nps.gov/api/v1/parks?q={}&limit=1000{}'.format(park_code, api_key)
    request = requests.get(api_request_link).json()
    try:
        park_description = request['data'][1]['description']
        city = request['data'][1]['addresses'][0]['city']
        state = request['data'][1]['addresses'][0]['stateCode']
        park_pic = request['data'][1]['images'][0]['url']

    except IndexError:
        park_description = request['data'][0]['description']
        city = request['data'][0]['addresses'][0]['city']
        state = request['data'][0]['addresses'][0]['stateCode']
        park_pic = request['data'][0]['images'][0]['url']

    entrance_fees_arr_length = len(request['data'][0]['entranceFees'])
    sum = 0
    counter = 0
    for each_cost_field in range(entrance_fees_arr_length):
        cost = request['data'][0]['entranceFees'][each_cost_field]['cost']
        sum = sum + float(cost)
        counter = counter + 1

    avg_cost = sum / counter

    return {
        "park_description": park_description,
        "park_name": request['data'][0]['name'],
        "avg_cost": round(avg_cost),
        "directions_url": request['data'][0]['directionsUrl'],
        "city": city,
        "state": state,
        "park_pic": park_pic
    }

def get_activities():
    api_request_link = 'https://developer.nps.gov/api/v1/activities?{}'.format(api_key)
    request = requests.get(api_request_link).json()
    activities = []

    for activity in range(len(request['data'])):
        activities.append(request['data'][activity]['name'])

    return activities

