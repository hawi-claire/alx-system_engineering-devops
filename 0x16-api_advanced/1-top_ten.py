#!/usr/bin/python3

"""
Write a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.

Requirements:
    - Prototype: def top_ten(subreddit)
    - If not a valid subreddit, print None.
    - Note: Invalid subreddits may return a redirect to search results.
      Ensure that you are not following redirects.
"""


from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and print the titles
    of the first 10 hot posts listed for a given subreddit

    Args:
        subreddit (str): The name of the subreddit

    Return:
        Void
    """

    if subreddit is None:
        return print("None")

    api_endpoint = 'https://reddit.com/r/{}/hot.json'.format(
        subreddit)

    response = get(api_endpoint, params={'limit': 10})

    if response.ok is False:
        return print("None")

    posts = response.json()

    for post in posts.get('data').get('children'):
        print(post.get('data').get('title'))
