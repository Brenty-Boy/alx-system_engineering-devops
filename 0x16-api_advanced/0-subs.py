#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Method get the number of users subscribed to a subreddit

    subreddit (Str)- subreddit to check

    Returns - number of users (INT) else 0 (INT) if not subreddit is found
    """
    try:
        headers = {
                "User-Agent": "win10_Pro:version.22H2 (by u/Brenty_Boy_180774)"
                }
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except Exception as e:
        return 0


if __name__ == "__main__":
    pass
