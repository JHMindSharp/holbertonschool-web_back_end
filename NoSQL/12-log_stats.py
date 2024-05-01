#!/usr/bin/env python3
"""
Module log_stats
Provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def print_nginx_stats():
    """
    Prints statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    print_nginx_stats()
