#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API and counts the occurrences of keywords
    in the titles of hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The 'after' parameter for pagination.
        word_counts (dict): A dictionary to store the word counts.
    """
    if word_counts is None:
        word_counts = {}
        for word in word_list:
            word_counts[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            if not posts:
                if any(word_counts.values()):
                    sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
                    for word, count in sorted_counts:
                        if count > 0:
                            print(f"{word}: {count}")
                return

            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    word_lower = word.lower()
                    for title_word in title.split():
                        if title_word == word_lower:
                            word_counts[word_lower] += 1

            after = data["data"]["after"]
            if after:
                count_words(subreddit, word_list, after, word_counts)
            else:
                sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")

        elif response.status_code == 404:
            return
        else:
            return

    except requests.exceptions.RequestException:
        return
    except (KeyError, ValueError):
        return
