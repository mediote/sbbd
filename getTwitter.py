from dotenv import load_dotenv
import urllib.request as urllib2
import pandas as pd
import requests
import json
import time
import os

load_dotenv()
auth_token = os.environ.get('AUTH_TOKEN')
header = {'Authorization': 'Bearer ' + auth_token}

class TwitterHook():

    def __init__(self, query, header = None, start_time = None, end_time = None, max_results= None):
        self.query = query
        self.header = header
        self.start_time = '2020-02-29T00%3A00%3A00Z'
        self.end_time = '2021-05-04T00%3A00%3A00Z'
        self.max_results = '500'

    def create_url(self):
        query = self.query
        start_time = self.start_time
        end_time = self.end_time        
        
        tweet_fields = "tweet.fields=author_id,id,created_at,in_reply_to_user_id,text"
        user_fields = "expansions=author_id&user.fields=id,name,username,created_at"
        start_time = (
            f"&start_time={self.start_time}"
            if self.start_time
            else ""
        )
        end_time = (
            f"&end_time={self.end_time}"
            if self.end_time
            else ""
        )
        max_results  = (
            f"&max_results={self.max_results}"
            if self.max_results
            else ""
        )
        url = "https://api.twitter.com/2/tweets/search/all?query={}&{}&{}{}{}{}".format(
               query, tweet_fields, user_fields, start_time, end_time, max_results
        )
        return url

    def connect_to_endpoint(self, url, header):
        response = requests.get(url,headers=header)
        listOfTweets = json.loads(response.content)
        return  listOfTweets


    def paginate(self, url, header, next_token=""):
        if next_token:
            full_url = f"{url}&next_token={next_token}"
            print('New Request on',full_url)
        else:
            full_url = url
            print('New Request on',full_url)
        data = self.connect_to_endpoint(full_url, header)
        yield data
        if "next_token" in data.get("meta", {}):
            yield from self.paginate(url, header, data['meta']['next_token'])


    def run(self):  
        url = self.create_url()
        yield from self.paginate(url, header)
        
        
def GetTweets(query):
    tweets = pd.DataFrame()
    for pg in TwitterHook(query).run():
        time.sleep(1)  
        
        if 'data' in pg:
            tweets =  tweets.append(pg['data'],ignore_index=True)
        else:
             print('Missing request')
        
    print('Done! Total of', len(tweets), 'tweets collected.')
    return tweets
