#!/usr/bin/python3
"""
This scrit has a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for a
given subreddit.
If an invalid subreddit is given, the function
returns 0.
"""
import json
import requests


def number_of_subscribers(subreddit):

    """This function to returns the number of subscribers"""
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "User Agent"}
    response = requests.get(url + subreddit + "/about.json",
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        x = response.json().get("data").get("subscribers")
        return response.json().get("data").get("subscribers")
    else:
        return 0
