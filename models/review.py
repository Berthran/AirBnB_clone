#!/usr/bin/python3
'''
A class simulation of a review inheriting from BaseModel class.

classes:
    Review
'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''A review class simulating a review'''

    place_id = ""
    user_id = ""
    text = ""
