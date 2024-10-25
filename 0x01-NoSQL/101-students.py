#!/usr/bin/env python3
"""Task 14"""
import pymongo


def top_students(mongo_collection):
    """Returns:
            all students sorted by avarage score
    """
    result = mongo_collection.find({})
    for doc in result:
        topics = doc.get('topics')
        summation = 0
        for topic in topics:
            summation += topic.get('score')
        avg = summation / len(topics)
        mongo_collection.find_one_and_update({"name": doc.get('name')},
                                             {'$set': {'averageScore': avg}})
        sort = mongo_collection.find().sort('averageScore', pymongo.DESCENDING)
    return sort
