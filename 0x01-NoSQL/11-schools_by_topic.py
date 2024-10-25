#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """Function returns list of students having specific topic"""
    list_schools = []
    result = mongo_collection.find({"topics": topic})
    for doc in result:
        list_schools.append(doc)
    return list_schools
