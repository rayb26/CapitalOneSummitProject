from flask import Blueprint, render_template, request, flash, make_response
from api.nps_api_functions import get_park_profile, get_activities, find_park_from_keyword
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@views.route('/find-activity', methods=['GET', 'POST'])
def find_activity():

    activities = get_activities()
    return render_template('activities.html', activities=activities)

@views.route('/find-park/<activity>', methods=['GET', 'POST'])
def activities_by_parks(activity):
    park_by_activity_dict = find_park_from_keyword(activity)
    parks = park_by_activity_dict.get('park_name')

    return render_template('parks_by_activity.html', parks=parks)



@views.route('/find-webcams', methods=['GET', 'POST'])
def find_webcams():
    return "<p> Hello world </p>"

@views.route('/park/<park_code>/', methods=['GET', 'POST'])
def park_info(park_code):
    park_profile = get_park_profile(park_code)
    park_name = park_profile.get('park_name')
    park_description = park_profile.get('park_description')
    avg_cost = park_profile.get('avg_cost')
    directions_url = park_profile.get('directions_url')
    city = park_profile.get('city')
    state = park_profile.get('state')
    park_pic = park_profile.get('park_pic')

    return render_template('park_info.html', park_name=park_name, park_description=park_description,
                           avg_cost=avg_cost, directions_url=directions_url, city=city, state=state, park_pic=park_pic)

@views.route('/show_map', methods=['GET', 'POST'])
def show_map():
    return "<p> Hello world </p>"
