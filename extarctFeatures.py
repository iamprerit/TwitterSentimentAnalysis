import preprocessTweets
import re
def getStopWordList(FileName):
	stopWords = []
	stopWords.append('AT_USER')
	stopWords.append('URL')
	fp = open(FileName, 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords
def replaceTwoOrMore(w):
	pattern=re.compile(r"(.)\1{1,}",re.DOTALL)
	return pattern.sub(r"\1\1",w)
def getFeatures(tweet):
	features=[]
	words=tweet.split()
	stopWords=getStopWordList("stopWordsFile.txt")
	for w in words:
		w=replaceTwoOrMore(w)
		w=w.strip('\'"?,.')
		val=re.search(r"^[a-zA-Z][a-zA-Z0-9]*$",w)
		if(w in stopWords or val is None):
			continue
		else:
			features.append(w.lower())
	return features
def extFeat(filename):
	csv_f=preprocessTweets.ppTweets(filename)
	test_f=[]
	ext_f=[]
	extracted_tweets=[]
	for row in csv_f:
		sentiment=row[1]
		tweet=row[0]
		features=getFeatures(tweet)
		extracted_tweets.append((features,sentiment))
		test_f.append(features)
	#print(extracted_tweets)
	for row in test_f:
		for col in row:
			ext_f.append(col)
	ext_f=list(set(ext_f))
	return (ext_f,extracted_tweets)	