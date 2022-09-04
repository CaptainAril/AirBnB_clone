#!/usr/bin/python3
"""This module defines a class Review."""
from .base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
