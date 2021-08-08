#! usr/bin/env python3
from classes.redditpull import reddit_pull

rp = reddit_pull()

try:
    r_connection = rp.read_connect()
    print('Success')
    print(r_connection)
except:
    print('Failed')

try:
    rp.read_top(r_connection,'legaladvice')
except Exception as e: 
    print(e)
    print('Read Failed')

try:
    rp.pull_sub_data(r_connection,'austin')
except Exception as e: 
    print(e)
    print('Read Failed')

