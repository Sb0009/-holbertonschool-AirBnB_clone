#!/usr/bin/env python3
"""This module contains the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ''
    user_id = ''
    text = ''
