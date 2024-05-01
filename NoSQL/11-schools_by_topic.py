#!/usr/bin/env python3
"""
Module schools_by_topic
Returns the list of schools having a specific topic.
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of schools matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass

