#!/usr/bin/env python
import random
import socket
import sys

import praw

class reddit_pull():
    def __init__(
        self
    ):
        self.file_read = ''

    #open connection to reddit
    def receive_connection(
        self
    ):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    #request token from PRAW
    def access_token(
        self
    ):
        try:
            #refresh_token='h'
            print('Refresh token success')
        except:
            print('Error-access_token function')

    def read_connect(
        self
    ):
        reddit_connection = praw.Reddit(client_id = 'kSMRAVneL-HuSg',
                            client_secret = '',
                            user_agent = 'michael-reddit-api-testing')
        print(reddit_connection.read_only) # output of this should be true
        return reddit_connection

    #For a specific subreddit, read the top posts.
    def read_top(
        self,
        reddit_connection,
        subreddit_name
    ):
        for submission in reddit_connection.subreddit(subreddit_name).top(limit=1):
            print(submission.title, submission.id)
