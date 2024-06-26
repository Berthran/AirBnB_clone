#!/usr/bin/python3
'''
A class simulation of a place inheriting from BaseModel class.

classes:
    Place
'''


from models.base_model import BaseModel


class Place(BaseModel):
    '''A place class simulating a place'''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
