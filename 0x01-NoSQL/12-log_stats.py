#!/usr/bin/env python3
"""12-log_stats.py"""

from pymongo import MongoClient


def log_stats():
    """Function displays nginx log statistics"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    call = client.logs.nginx
    logs = call.count_documents({})
    get_req = call.count_documents({"method": "GET"})
    post_req = call.count_documents({"method": "POST"})
    put_req = call.count_documents({"method": "PUT"})
    patch_req = call.count_documents({"method": "PATCH"})
    del_req = call.count_documents({"method": "DELETE"})
    get_path = call.count_documents({"method": "GET", "path": "/status"})
    res = f'{logs} logs\nMethods:\n\tmethod GET: {get_req}\n\t'
    res1 = f'method POST: {post_req}\n\tmethod PUT: {put_req}\n\t'
    res2 = f'method PATCH: {patch_req}\n'
    res3 = f'\tmethod DELETE: {del_req}\n{get_path} status check'
    final = res + res1 + res2 + res3
    print(final)


if __name__ == "__main__":
    log_stats()
