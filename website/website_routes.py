from flask import Blueprint, render_template, request, flash, make_response
from api.nps_api_functions import get_park_profile, get_activities, find_park_from_keyword, get_parks, get_tags

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

    return render_template('parks_by_activity.html', parks=parks, activity=activity)


@views.route('/find-parks', methods=['GET', 'POST'])
def find_parks():
    return render_template('find_parks.html', parks=get_parks().get('parks'))


@views.route('/park/<park_code>/', methods=['GET', 'POST'])
def park_info(park_code):
    park_code = __convert_park_code_from_name__(park_code)

    park_profile = get_park_profile(park_code)
    park_name = park_profile.get('park_name')
    park_description = park_profile.get('park_description')
    avg_cost = park_profile.get('avg_cost')
    directions_url = park_profile.get('directions_url')
    city = park_profile.get('city')
    state = park_profile.get('state')
    park_pic = park_profile.get('park_pic')
    tags = get_tags(park_code)

    if avg_cost == 0:
        avg_cost = 'Free'
    else:
        avg_cost = '$' + str(avg_cost)

    return render_template('park_info.html', park_name=park_name, park_description=park_description,
                           avg_cost=avg_cost, directions_url=directions_url, city=city, state=state, park_pic=park_pic,
                           tags=tags)


@views.route('/show_map', methods=['GET', 'POST'])
def show_map():
    return "<p> Hello world </p>"


def __convert_park_code_from_name__(park_name):
    park_dict = get_parks()
    park_list = park_dict.get('parks')
    park_code_list = park_dict.get('park_codes')

    for park in range(len(park_list)):
        if park_list[park] == park_name:
            return park_code_list[park]

    return None
