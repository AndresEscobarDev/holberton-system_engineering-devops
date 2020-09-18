#!/usr/bin/python3
""" Task 0 """


def top_ten(subreddit):
    """ Function that queries the Reddit API
    and returns the number of subscribers """
    import requests

    info = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        headers={"User-Agent": "Andres-agent"},
                        allow_redirects=False)
    if info.status_code == 200:
        subscribers = info.json().get('data').get('children')
        print('\n'.join(subscribers[i].get('data').get('title')
              for i in range(10)))
    else:
        print('None')
