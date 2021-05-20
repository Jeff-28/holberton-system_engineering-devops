#!/usr/bin/python3
'''A python script to use Reddit's API'''
import requests


def recurse(subreddit, hot_list=[], after=1):
    '''Returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, return None.'''
    site = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    head = {'User-Agent': 'I am a Shield Agent'}
    response = requests.get(site, headers=head, params={'after': after})
    try:
        if response.status_code != 200:
            return None
        if after is None:
            return hot_list
        data_dic = response.json()
        data_list = data_dic['data']['children']
        for value in data_list:
            hot_list.append(value['data']['title'])
        return recurse(subreddit, hot_list, data_dic['data']['after'])
    except:
        pass
