#!/usr/bin/python3
"""
Module that contains a recursive function
that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of
    all hot articles for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    url = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
                       headers={'User-Agent': 'Python/requests:APIproject:\
                       v1.0.0 (by /u/abukiplimo)'},
                       params={'after': after}).json()
    after = url.get('data', {}).get('after', None)
    posts = url.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
