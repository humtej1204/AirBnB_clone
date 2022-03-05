#!/usr/bin/python3

'''File with the class Review'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Review Class'''
    place_id = ""
    user_id = ""
    text = ""
