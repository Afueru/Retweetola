import tweepy

consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#USER ID do guto: 0000000000
guto = "XXXXXXXXXXX"
gutoid = 00000000000
first = False
if first == True:
	api.create_friendship(guto)
	gutweets = api.user_timeline(screen_name = guto,count = 200, include_rts = False, tweet_mode = 'extended')
	gutweets.reverse()
	for tweet in gutweets:
		api.retweet(tweet.id)
else:
	gutweets = api.user_timeline(screen_name = guto, count = 15, tweet_mode = 'extended')
	gutweets.reverse()
	for tweet in gutweets:
		rt = "RT @"
		#print("chech")
		if rt not in tweet.full_text and tweet.retweeted == False:
			#print("Tweet anterior: " + gutweets[gutweets.index(tweet) - 1].full_text)
			api.retweet(tweet.id)
			print("Tweet: " + tweet.full_text)
			print("Retweetolado!")
			#print("Tweet posterior: " + gutweets[gutweets.index(tweet) + 1].full_text)
"""else:
	new_gutweets = api.user_timeline(screen_name = guto, count = 5, include_rts = False, tweet_mode = 'extended')
	new_gutweets.reverse()
	for tweet in new_gutweets:
		if tweet.retweeted == False:
			api.retweet(tweet.id)
			print("Retweetolado!")"""
"""gutweets_testing = api.user_timeline(screen_name = guto, count = 20, tweet_mode = 'extended')
for tweet in gutweets_testing:
	if tweet.entities["urls"] != []:
		print("Tweet anterior: " + gutweets_testing[gutweets_testing.index(tweet) - 1].full_text)
		print("Tweet: " + tweet.full_text)
		print("Tweet posterior: " + gutweets_testing[gutweets_testing.index(tweet) + 1].full_text)"""

	
exit()





	


