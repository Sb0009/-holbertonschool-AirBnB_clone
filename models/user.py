#!/usr/bin/env python3
"""This module contains the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
