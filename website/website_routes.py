from flask import Blueprint, render_template, request, flash, make_response
import api.nps_api_functions
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@views.route('/find-activity', methods=['GET', 'POST'])
def find_activity():
    return "<p> Hello world </p>"

@views.route('/find-webcams', methods=['GET', 'POST'])
def find_webcams():
    return "<p> Hello world </p>"

@views.route('/park/<park_code>/', methods=['GET', 'POST'])
def park_info(park_code):
    park_profile = api.nps_api_functions.get_park_profile(park_code)

    return render_template('park_info.html', park_name=park_code)

@views.route('/show_map', methods=['GET', 'POST'])
def show_map():
    return "<p> Hello world </p>"
