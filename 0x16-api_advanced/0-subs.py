#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
    except KeyError:
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit = "programming"
    print(f"Number of subscribers in subreddit '{subreddit}': {number_of_subscribers(subreddit)}")
    
    subreddit = "this_is_a_fake_subreddit"
    print(f"Number of subscribers in subreddit '{subreddit}': {number_of_subscribers(subreddit)}")
