#!/usr/bin/python3
"""
This is a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None
"""
from requests import get


def recurse(subreddit, hot_list=[], page=None):
    """returns a list containing the titles of all hot articles
    for a given subreddit"""

    if page is None:
        request = get('https://www.reddit.com/r/{}/hot.json'
                      .format(subreddit), headers={'User-Agent': 'jdarangop'},
                      allow_redirects=False)
    else:
        request = get('https://www.reddit.com/r/{}/hot.json?after={}'
                      .format(subreddit, page),
                      headers={'User-Agent': 'jdarangop'},
                      allow_redirects=False)

    if request.status_code != 200:
        return None
    else:
        after = request.json().get('data').get('after')
        list_post = request.json().get('data').get('children')
        for i in list_post:
            hot_list.append((i.get('data').get('title')))
        if after:
            return(recurse(subreddit, hot_list, after))
        else:
            return hot_list
