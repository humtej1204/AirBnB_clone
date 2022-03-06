#!/usr/bin/python3
'''
    Contains the TestPlaceDocs classes
'''
import os
from datetime import datetime
import inspect
import models
from models import place
from models.base_model import BaseModel
import pep8
import unittest
Place = place.Place
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestPlaceDocs(unittest.TestCase):
    '''
        Tests to check the documentation and style of Place class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Set up for the doc tests
        '''
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        '''
            Test that models/place.py conforms to PEP8
        '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        '''
            Test for the place.py module docstring
        '''
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        '''
            Test for the Place class docstring
        '''
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")


class TestPlace(unittest.TestCase):
    '''
        Test the Place class
    '''
    def test_is_subclass(self):
        '''
            Test that Place is a subclass of BaseModel
        '''
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        '''
            Test Place has attr city_id, and it's an empty string
        '''
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if storage_t == "db":
            self.assertEqual(place.city_id, None)
        else:
            self.assertEqual(place.city_id, None)

    def test_user_id_attr(self):
        '''
            Test Place has attr user_id, and it's an empty string
        '''
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if storage_t == "db":
            self.assertEqual(place.user_id, None)
        else:
            self.assertEqual(place.user_id, None)

    def test_name_attr(self):
        '''
            Test Place has attr name, and it's an empty string
        '''
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if storage_t == "db":
            self.assertEqual(place.name, None)
        else:
            self.assertEqual(place.name, None)

    def test_description_attr(self):
        '''
            Test Place has attr description, and it's an empty string
        '''
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if storage_t == "db":
            self.assertEqual(place.description, None)
        else:
            self.assertEqual(place.description, None)

    def test_number_rooms_attr(self):
        '''
            Test Place has attr number_rooms, and it's an int == 0
        '''
        pass

    def test_number_bathrooms_attr(self):
        '''
            Test Place has attr number_bathrooms, and it's an int == 0
        '''
        pass

    def test_max_guest_attr(self):
        '''
            Test Place has attr max_guest, and it's an int == 0
        '''
        pass

    def test_price_by_night_attr(self):
        '''
            Test Place has attr price_by_night, and it's an int == 0
        '''
        pass

    def test_latitude_attr(self):
        '''
            Test Place has attr latitude, and it's a float == 0.0
        '''
        pass

    def test_longitude_attr(self):
        '''
            Test Place has attr longitude, and it's a float == 0.0
        '''
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if storage_t == "db":
            self.assertEqual(place.longitude, None)
        else:
            self.assertEqual(place.longitude, None)

    @unittest.skipIf(storage_t == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        '''
            Test Place has attr amenity_ids, and it's an empty list
        '''
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        '''
            Test to_dict method creates a dictionary with proper attrs
        '''
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        '''
            Test that values in dict returned from to_dict are correct
        '''
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        '''
            Test that the str method has the correct output
        '''
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
