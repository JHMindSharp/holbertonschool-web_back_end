#!/usr/bin/env python3
"""
Module update_topics
Updates all topics of a school document based on its name.
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics to add.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
