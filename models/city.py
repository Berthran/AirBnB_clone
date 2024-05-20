#!/usr/bin/python3
'''
A class simulation of a city inheriting from BaseModel class.

classes:
    City
'''


from models.base_model import BaseModel


class City(BaseModel):
    '''A city class simulating a city'''

    state_id = ""
    name = ""
