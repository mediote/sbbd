
#from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import requests
import json
import time
#import os


class TwitterHook():
    
    def __init__(self, auth_token, base_url, query, start_time = None, end_time = None, max_results= None):
        self.query = query
        self.start_time = start_time
        self.end_time = end_time
        self.base_url = base_url
        self.auth_token = auth_token
        self.max_results = '500'

        #load_dotenv()
        #auth_token = os.environ.get('AUTH_TOKEN')
        header = {'Authorization': 'Bearer '+auth_token}
        self.header = header

    def create_url(self):

        query = self.query  
        base_url = self.base_url

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

        tweet_fields = "tweet.fields=author_id,id,created_at,in_reply_to_user_id,text"
        
        #https://api.twitter.com/2/tweets/search/all
        url = "{}?query={}&{}{}{}{}".format(
               base_url, query, tweet_fields, start_time, end_time, max_results
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
        data = self.connect_to_endpoint(full_url,header)
        yield data
        if "next_token" in data.get("meta", {}):
            yield from self.paginate(url,header, data['meta']['next_token'])


    def run(self):  
        url = self.create_url()
        yield from self.paginate(url, self.header)
        
        
def GetTweets(uth_token, base_url,query, start_time, end_time):
    tweets = pd.DataFrame()
    for pg in TwitterHook(uth_token, base_url, query, start_time, end_time).run():
        time.sleep(1)  
              
        if 'data' in pg:
            tweets =  tweets.append(pg['data'],ignore_index=True)      
        else:            
            st.error('Missing request')

    st.success('Total of {} tweets collected.'.format(len(tweets)))
    return tweets