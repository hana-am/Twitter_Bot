from secrets import *
import twitter
import codecs
import sys

# we read our keys to connect to twitter api
api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, 
                access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)

# we use method called GetStatus to get detials about a specific status writter in twitter
statuses = api.GetStatus(898442237381455873)
mentions_list= api.GetMentions()
#mentions_list[0] = '1'
print(len(mentions_list))