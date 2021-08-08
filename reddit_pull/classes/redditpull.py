#!/usr/bin/env python
import random
import socket
import sys
import boto3
import praw
import json

#for converting to unix timestamp
import time

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
                            client_secret = '0G_UUftkHWr2fpzBaXYZTgphyU8',
                            user_agent = 'michael-reddit-api-testing')
        print(reddit_connection.read_only) # output of this should be true
        return reddit_connection

    #For a specific subreddit, read the top 1 posts.
    def read_top(
        self,
        reddit_connection,
        subreddit_name
    ):
        for submission in reddit_connection.subreddit(subreddit_name).top(limit=1):
            print(submission.title, submission.id)

    #Pull the data for top sub and drop in a specific S3 location.
    def pull_sub_data(
        self,
        reddit_connection,
        subreddit_name,
        s3_location
    ):
        reddit_data = {}
        count = 0
        session = boto3.Session(
            aws_access_key_id = '',
            aws_secret_access_key = ''
        )

        s3 = session.resource('s3')
        #landing_bucket = s3.Bucket(s3_location)
        for submission in reddit_connection.subreddit(subreddit_name).controversial(limit=10):
            count += 1
            try:
                reddit_data[count] = ({
                   "id":submission.id,
                   "title":submission.title,
                   "url":submission.url,
                   "create_date":submission.created_utc,
                   "subreddit":submission.subreddit.display_name
                })
            except Exception as ex:
                print(ex)

        #print(json.dumps(reddit_data))
        s3.Object(s3_location,subreddit_name+str(time.time())+'.json').put(Body=json.dumps(reddit_data))