#!/usr/bin/python3
'''A python script to use Reddit's API'''
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0"""
    site = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'User-Agent': 'I am a Shield Agent'}
    response = requests.get(site, headers=head)
    try:
        if response.status_code != 200:
            return 0
        return response.json()['data']['subscribers']
    except:
        return 0
