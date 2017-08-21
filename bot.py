from secrets import *
import twitter
import codecs
import sys
from TwitterAPI import TwitterAPI
# we read our keys to connect to twitter api
api = TwitterAPI(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, 
                access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
"""
r = api.request('statuses/show/:%d' % 898442237381455873)
for item in r.get_iterator():
    print(item['text'])
"""
'''
print("============================")
username= 'ThisArchive'
original_tweet= 898442237381455873
r = api.request('search/tweets', {'q':'to:%s' % username})
for k in r.get_iterator():
    if k['in_reply_to_status_id'] == original_tweet:
        print(k['text'])
'''
username= 'ZainB'
original_tweet= 898185380981288960
r = api.request('search/tweets', {'q':'to:%s' % username})
for k in r.get_iterator():
    if k['in_reply_to_status_id'] == original_tweet :
        print(k['text'])
        #print(k['user']['screen_name'])