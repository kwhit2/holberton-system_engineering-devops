#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None """
import json
import requests
from sys import argv


def recurse(subreddit, hot_list=[]):
    """ recurse method """
