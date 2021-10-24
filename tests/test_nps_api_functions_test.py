from unittest import TestCase
from api.nps_api_functions import find_park_from_keyword, get_coordinates, get_park_profile, get_activities


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
        print(function_dict_as_str)
        assert 'Spread across a wild landscape' in function_dict_as_str
        assert 'Acadia' in function_dict_as_str
        assert '23' in function_dict_as_str
        assert 'http://www.nps.gov/acad/planyourvisit/directions.htm' in function_dict_as_str
        assert 'ME' in function_dict_as_str
        assert 'Patten' in function_dict_as_str
        assert 'https://www.nps.gov/common/uploads/structured_data/706CD3A6-9835-C974-F5C1ECDF3354177B.jpg' in function_dict_as_str

    def test_get_activities(self):
        activity_list = get_activities()
        assert len(activity_list) == 40
        assert 'Swimming' in activity_list
        assert 'Skiing' in activity_list
        assert 'Canyoneering' in activity_list



