#!/usr/bin/env python3
""" Task 9 """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Function inserts a new document in  a collection
    Returns:
        _id: new id of the result
    """
    result = mongo_collection.insert_one({**kwargs})
    return result.inserted_id
