#!/usr/bin/env python3
"""
Module list_all
Lists all documents in a collection.
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of all documents in the collection.
    """
    return list(mongo_collection.find())


if __name__ == "__main__":
    pass
