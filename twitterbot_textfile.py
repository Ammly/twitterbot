#Import our Twitter credentials from credentials.py
import tweepy
from time import sleep
from credentials import *

#Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Open text file verne.txt for reading
my_file = open('verne.txt', 'r')

#Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

#Close file
my_file.close()

def tweet():
	#Iterate over file_lines
	for line in file_lines:
	    try:
	        print(line)

	#Skip if line is blank
	        if line != '\n':
	            api.update_status(line)

	        else:
	            pass
	    except tweepy.TweepError as e:
	        print(e.reason)

	#Space tweets by 15 minutes each
	    sleep(900)

tweet()