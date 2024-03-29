#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0 """
import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ number_of_subscribers method """
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    agent_string = "API-practice-holberton-cardano"

    subs = requests.get(url, headers={'User-Agent': agent_string})

    if subs.status_code != 200:
        return (0)
    else:
        json_response = subs.json()
        sub_count = json_response.get('data').get('subscribers')
        return sub_count
