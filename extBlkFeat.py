import extarctFeatures
import preprocessTweets
import nltk
def extBlk():
	whole=extarctFeatures.extFeat("sampleTweets.csv")
	tweets=whole[1]
	training_set=nltk.classify.util.apply_features(extract_features,tweets)
	NBClassifier=nltk.NaiveBayesClassifier.train(training_set)
	testTweet = 'Disappointing day. my arm hurts'
	processedTestTweet=preprocessTweets.processTweet(testTweet)
	print (NBClassifier.classify(extract_features(extarctFeatures.getFeatures(processedTestTweet))))
	#print (NBClassifier.show_most_informative_features(20))
def extract_features(tweet):
    tot=extarctFeatures.extFeat("sampleTweets.csv")
    featureList=tot[0]
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
extBlk()