#!/usr/bin/python3
"""
Module that contains a function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={'User-Agent': 'Python/requests:APIproject\
                       :v1.0.0 (by /u/abukiplimo)'}).json()
    subs = url.get("data", {}).get("subscribers", 0)
    return subs
