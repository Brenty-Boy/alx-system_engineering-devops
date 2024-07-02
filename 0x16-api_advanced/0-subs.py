#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'my-reddit-app:v1.0 (by /u/Brenty_Boy_180774)'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        # Raise HTTPError for bad responses (4xx or 5xx)
        results = response.json()
        return results['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
    except (KeyError, TypeError) as e:
        print(f"Error parsing JSON: {e}")
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(
                f"Number of subscribers in r/{subreddit}:
                {number_of_subscribers(subreddit)}"
                )
