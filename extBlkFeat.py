import extarctFeatures
import preprocessTweets
import nltk
def extBlk(filename):
	whole=extarctFeatures.extFeat("traindata1.csv")
	tweets=whole[1]
	training_set=nltk.classify.util.apply_features(extract_features,tweets)
	NBClassifier=nltk.NaiveBayesClassifier.train(training_set)
	f1=open(filename)
	f2=open('finalResults.txt','w')
	for x in f1.readlines():
		testTweet = x
		processedTestTweet=preprocessTweets.processTweet(testTweet)
		res=NBClassifier.classify(extract_features(extarctFeatures.getFeatures(processedTestTweet)))
		f2.write(x+'  '+res+'\n')
	f1.close()
	f2.close()
def extract_features(tweet):
    tot=extarctFeatures.extFeat("traindata1.csv")
    featureList=tot[0]
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features