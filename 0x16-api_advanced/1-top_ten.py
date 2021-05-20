#!/usr/bin/python3
'''A python script to use Reddit's API'''
import requests


def top_ten(subreddit):
    '''Prints the titles of the first 10 hot posts listed for a given
    subreddit'''
    site = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    head = {'User-Agent': 'I am a Shield Agent'}
    response = requests.get(site, headers=head)
    try:
        if response.status_code != 200:
            print('None')
        data_dic = response.json()
        data_list = data_dic['data']['children']
        for value in data_list[:10]:
            print(value['data']['title'])
    except:
        pass
