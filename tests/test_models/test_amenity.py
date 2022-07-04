#!/usr/bin/python3

"""Module that tests the amenity class
"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestAmenity Class
    """

    def test_create_amenity(self):
        """Test when  a amenity is created
        """

        my_model = Amenity()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'Amenity')
