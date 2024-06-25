#!/usr/bin/python3
"""This script will return the number of subscribers associated with
a subreddit
"""
import json
import requests
from sys import argv


def top_ten(subreddit):
    """Method get the number of users subscribed to a subreddit

    subreddit (Str)- subreddit to check

    Returns - number of users (INT) else 0 (INT) if not subreddit is found
    """
    try:
        headers = {
                'User-Agent': 'win10_Pro:version.22H2 (by u/Brenty_Boy_180774)'
                }
        p = {'limit': 10}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(
                url, headers=headers, params=p,
                allow_redirects=False
                ).json().get('data')

        for post in req.get('children'):
            print(post.get('data', None).get('title', None))

    except Exception as e:
        print(None)


if __name__ == "__main__":
    pass
