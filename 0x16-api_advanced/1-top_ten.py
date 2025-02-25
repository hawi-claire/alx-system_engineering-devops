#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        elif response.status_code == 404:
            print(None)
        else:
            print(None)

    except requests.exceptions.RequestException:
        print(None)
    except (KeyError, ValueError):
        print(None)
