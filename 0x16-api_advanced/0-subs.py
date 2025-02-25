#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        return 0
    except requests.exceptions.RequestException as e:
        return 0
    except KeyError:
        return 0
    except ValueError:
        return 0
