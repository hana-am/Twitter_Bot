from secrets import *
import twitter
import codecs
import sys


api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, 
                access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
statuses = api.GetStatus(898425485608210432)

print(statuses)