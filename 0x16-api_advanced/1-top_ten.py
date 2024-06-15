#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests
import json


def top_ten(subreddit):
    headers = {
        "User-Agent": "linux:0x16-api_advanced:v1.0 (by /u/Brenty_Boy_180774)"
    }
    url = 'https://www.reddit.com/r/{:}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code indicates a successful response
    if r.status_code == 200:
        # Check if the response content type is JSON
        if 'application/json' in r.headers.get('Content-Type', ''):
            try:
                data_dict = r.json().get('data')
                hot_list = data_dict.get('children')
                for post in hot_list:
                    sub_data_dict = post.get('data')
                    print(sub_data_dict.get('title'))
            except json.JSONDecodeError:
                print("Failed to decode JSON from response.")
        else:
            print("The response is not in JSON format.")
    else:
        print(None)
