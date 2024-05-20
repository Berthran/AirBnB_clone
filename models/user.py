#!/usr/bin/python3
'''
A class simulation of a user inheriting from BaseModel class.

classes:
    User
'''


from models.base_model import BaseModel


class User(BaseModel):
    '''A user class simulating a user'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
