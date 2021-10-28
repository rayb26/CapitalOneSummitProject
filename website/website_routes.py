"""
Author: Rayhan Biju
Version: October 27, 2021
Description: This file contains the logic for constructing each endpoint accessible to the client and passes in
various data points from the api/nps_api_functions.py file that parses the National Park Service API
"""
from flask import Blueprint, render_template
from api.nps_api_functions import get_park_profile, get_activities, find_park_from_keyword, get_parks, get_tags, \
    grab_webcam_metadata

views = Blueprint('views', __name__)

"""
Function contains logic to show the index.html page if the '/' directory is accessed by the client
"""


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


"""
Function contains logic to show the activities.html page if the '/find-activity' directory is accessed by the client
"""


@views.route('/find-activity', methods=['GET', 'POST'])
def find_activity():
    activities = get_activities()
    return render_template('activities.html', activities=activities)


"""
Function contains logic to show the parks_by_activity.html page if the '/find-park/<activity>' directory is 
accessed by the client, and the '<activity>' value represents a parameter than can be passed in by the client. 
Also, a list of the park names and activity type is passed into the 'parks_by_activity.html' page to be later 
manipulated by the Jinja2 framework.
"""


@views.route('/find-park/<activity>', methods=['GET', 'POST'])
def activities_by_parks(activity):
    park_by_activity_dict = find_park_from_keyword(activity)
    parks = park_by_activity_dict.get('park_name')

    return render_template('parks_by_activity.html', parks=parks, activity=activity)


"""
Function contains logic to show the find_parks.html page if '/find-parks' is passed by the client and a list of parks
is passed into the front-end to be manipulated by the Jinja2 framework. 
"""


@views.route('/find-parks', methods=['GET', 'POST'])
def find_parks():
    return render_template('find_parks.html', parks=get_parks().get('parks'))


"""
Function contains logic to show the park_info.html page if '/page/<park_code/' is passed by client. The <park_code>
parameter represents the specific park name that each park has. However, this name needs to be converted into the park's
code, which will then be passed into the appropriate functions to obtain park related data. Once this data has been 
fetched, it will be passed to the front-end and manipulated using the Jinja2 framework. 

"""


@views.route('/park/<park_code>/', methods=['GET', 'POST'])
def park_info(park_code):
    # Park name must be converted to the park name
    park_code = __convert_park_code_from_name__(park_code)
    webcams = grab_webcam_metadata(park_code)

    park_profile = get_park_profile(park_code)
    park_name = park_profile.get('park_name')
    park_description = park_profile.get('park_description')
    avg_cost = park_profile.get('avg_cost')
    directions_url = park_profile.get('directions_url')
    city = park_profile.get('city')
    state = park_profile.get('state')
    park_pic = park_profile.get('park_pic')
    tags = get_tags(park_code)
    # Handles case where the average ticket price is 0, so 'free' should be shown to the client
    if avg_cost == 0:
        avg_cost = 'Free'
    else:
        avg_cost = '$' + str(avg_cost)

    return render_template('park_info.html', park_name=park_name, park_description=park_description,
                           avg_cost=avg_cost, directions_url=directions_url, city=city, state=state, park_pic=park_pic,
                           tags=tags, webcams=webcams)


@views.route('/show_map', methods=['GET', 'POST'])
def show_map():
    return "<p> Hello world </p>"


"""
Private function converts a park's name to its corresponding park code and returns None if the park's code does not 
exist. 
"""


def __convert_park_code_from_name__(park_name):
    park_dict = get_parks()
    park_list = park_dict.get('parks')
    park_code_list = park_dict.get('park_codes')

    for park in range(len(park_list)):
        if park_list[park] == park_name:
            return park_code_list[park]

    return None
