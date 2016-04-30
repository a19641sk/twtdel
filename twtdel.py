import tweepy
import sys, time, csv, webbrowser

consumer_key = 'Your consumer_key'
consumer_secret = 'Your consumer_secret_key'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
redirect_url = auth.get_authorization_url()
webbrowser.open_new(redirect_url)
print ('Write your PIN code on console')
verifier = input()
auth.get_access_token(verifier)

access_token = auth.access_token
access_token_secret = auth.access_token_secret
#print ("access_token : ",access_token,"\n access_token_secret :",access_token_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print ('Write down your tweets CSV files directory include the CSV files name')
csv_file_directory = input()
csv_file = open(csv_file_directory,'r')
reader = csv.reader(csv_file)
tweets = [ row[0] for row in reader ]

if 'tweet_id' in tweets:
	del tweets[tweets.index('tweet_id')]

error = []
j = 0
l = len(tweets)
for i in tweets:
	j = j + 1
	try:
		api.destroy_status(i)
	except tweepy.error.TweepError:
		error.append(i)
		pass
	finally :
		sys.stdout.write('\r%d / %d, %f%% in progress' %(j,l,100*j/l))
		sys.stdout.flush()

if len(error) == 0:
	print ('There is no error. This program could delete your whole tweets')
else :
	print ('There are some errors to delte your tweets.\n This program deletes whole tweets, which doesn\'t occur problem')