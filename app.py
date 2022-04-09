import streamlit as st
import pandas as pd
import time
import getTwitter as tw
import urllib.request as urllib2
import streamlit as st
import pandas as pd


# ((vaccine vaccination) OR (vaccine OR vaccination)) place_country:US -is:retweet
#df = pd.read_csv('./vacinaobrigatorianao.csv', low_memory=False)

tweets = pd.DataFrame()


with st.form("form_search"):

    auth_token = st.text_input(
    "Auth token"
    )

    base_url = st.text_input(
    "Endpoint Url"
    )

    start_time = st.date_input(
    "Start time"
    )
   
    end_time = st.date_input(
    "End time"
    )
 
    start_time = urllib2.quote(start_time.strftime('%Y-%m-%dT%H:%M:%SZ'))
    end_time = urllib2.quote(end_time.strftime('%Y-%m-%dT%H:%M:%SZ'))
    
    query = st.text_input("Query",'')
    query = urllib2.quote(query)

    submitted = st.form_submit_button("Start/Stop")    
    
    if submitted:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            tweets = tw.GetTweets(auth_token, base_url, query, start_time, end_time)
            st.write(tweets.head(20))
        

@st.cache
def convert_df(tweets):
    return tweets.to_csv().encode('utf-8')

csv = convert_df(tweets)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='tweets.csv',
     mime='text/csv',
)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    with st.spinner('Wait for it...'):
        tweets = pd.read_csv(uploaded_file)
        st.write(tweets)
    st.success('Done!')