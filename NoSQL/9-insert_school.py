#!/usr/bin/env python3
"""
Module insert_school
Inserts a new document into a collection based on kwargs.
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Key-value pairs to be inserted as document fields.

    Returns:
        The ID of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id


if __name__ == "__main__":
    pass
