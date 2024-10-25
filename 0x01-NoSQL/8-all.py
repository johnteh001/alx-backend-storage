#!/usr/bin/env python3
""" Task 8 """
from pymongo import MongoClient


def list_all(mongo_collection):
    """Function list all documents in collection"""
    ret_list = []
    for doc in mongo_collection.find():
        ret_list.append(doc)
    return ret_list
