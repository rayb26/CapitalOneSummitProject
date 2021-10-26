from unittest import TestCase
from api.nps_api_functions import find_park_from_keyword, get_coordinates, get_park_profile, get_activities, get_parks, \
    get_tags, grab_webcam_metadata


class Test(TestCase):

    def test_find_park_by_keyword(self):
        function_dict_as_str = str(find_park_from_keyword('hiking'))

        assert 'Acadia' in function_dict_as_str
        assert 'Antietam' in function_dict_as_str
        assert len(function_dict_as_str) > 0
        assert 'alka' in function_dict_as_str
        assert 'https://www.nps.gov/alka/index.htm' in function_dict_as_str

    def test_get_coordinates(self):
        function_dict_as_str = str(get_coordinates('acad'))

        assert 'latitude' in function_dict_as_str
        assert 'longitude' in function_dict_as_str
        assert '44.409286' in function_dict_as_str
        assert '-68.247501' in function_dict_as_str

    def test_get_park_profile(self):

        function_dict_as_str = str(get_park_profile('acad'))
        assert 'Acadia National Park protects the natural beauty' in function_dict_as_str
        assert 'Acadia' in function_dict_as_str
        assert 'Acadia National Park' in function_dict_as_str
        assert '23' in function_dict_as_str
        assert 'http://www.nps.gov/acad/planyourvisit/directions.htm' in function_dict_as_str
        assert 'ME' in function_dict_as_str
        assert 'Bar Harbor' in function_dict_as_str
        assert 'https://www.nps.gov/common/uploads/structured_data/3C7B45AE-1DD8-B71B-0B7EE131C7DFC2F5.jpg' in function_dict_as_str

    def test_get_activities(self):
        activity_list = get_activities()
        assert len(activity_list) == 40
        assert 'Swimming' in activity_list
        assert 'Skiing' in activity_list
        assert 'Canyoneering' in activity_list

    def test_get_parks(self):
        parks_list = get_parks()

        assert 'Acadia National Park' in str(parks_list)
        assert len(parks_list) > 0
        assert 'African American Civil War Memorial' in str(parks_list)

    def test_get_things_to_do(self):
        things_to_do = get_tags('yell')
        assert 'Yellowstone National Park' in things_to_do
        assert len(things_to_do) > 0
        assert 'trail' in things_to_do
        assert 'moderate hike' in things_to_do

    def test_grab_webcam_data(self):
        web_cam_data = grab_webcam_metadata('acad')
        assert len(web_cam_data) > 0
        assert '.jpg' in str(web_cam_data)
        web_cam_data = grab_webcam_metadata('adam')
        assert len(web_cam_data) == 0
        assert '.jpg' not in str(web_cam_data)


