#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    headers = {
        "User-Agent": "linux:0x16-api_advanced:v1.0 (by /u/Brenty_Boy_180774)"
    }
    r = requests.get('https://www.reddit.com/r/{:}/hot.json?limit=10'.format(
        subreddit), headers=headers, allow_redirects=False)
    if r.status_code < 300:
        json = r.json()
        data_dict = json.get('data')
        hot_list = data_dict.get('children')
        for post in hot_list:
            sub_data_dict = post.get('data')
            print(sub_data_dict.get('title'))
    else:
        print(None)
