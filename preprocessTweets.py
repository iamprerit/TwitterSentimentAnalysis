import re
import readCSV
def ppTweets(filename):
	csv_f=readCSV.readfile(filename)
	csv_s=[]
	for row in csv_f:
		tweet = row[1]
		row[1]=processTweet(tweet)
		csv_s.append((row[1],row[0]))
	return csv_s
	

def processTweet(tweet):
	tweet=tweet.lower()
	tweet=re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
	tweet=re.sub('@[^\s]+','AT_USER',tweet)
	tweet=re.sub('[\s]+',' ',tweet)
	tweet=re.sub(r'#([^\s]+)',r'\1',tweet)
	tweet=tweet.strip('\'"')
	return tweet
