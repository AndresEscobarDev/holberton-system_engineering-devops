#!/usr/bin/python3
""" Task 0 """


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API
    and returns the number of subscribers """
    import requests

    info = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "Andres-agent"},
                        allow_redirects=False)
    if info.status_code == 200:
        return info.json().get('data').get('subscribers')
    return 0
