#Import Tweep, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

#Access and authorize our Twitter credentials rom credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#iterate over tweets with #laravel, limit to 10 / ,geocode='-1.2832533,36.8172449 ,100km'
for tweet in tweepy.Cursor(api.search, 
							q='#Laravel',
							result_type='recent',
							since='2018-02-08',
							lang='en').items(10):
	try:
		#print usernames of the last 10 people to use #laravel
		print('Tweet by: @' + tweet.user.screen_name)

		#Retweet tweets as they are found
		tweet.retweet()
		print('Retweeted the tweet')

		#Favorite the tweet
		tweet.favorite()
		print('Favorited the tweet')

		if not tweet.user.following:
			#Follow the user who tweeted
			tweet.user.follow()
			print('Followed the user')

		sleep(900)

	except tweepy.TweepError as e:
		print(e.reason)
	
	except StopIteration:
		break