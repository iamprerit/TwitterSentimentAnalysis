from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key="zNT5w8JAmKld3hHMdEcgRUoYR"
consumer_secret="D8xOlo71OZCsFruD8COZfg3yDR6VZ0IqAkqb9LRIfoAxEc0jTW"
access_token="78908940-xxZ3yeCGf4sr16F9ZLIiJBmbAMeo4lx2qBQmHsK48"
access_token_secret="RXA43aa3JWlVCg9O4QqpLMrVf6ABjgJJdow5mIem4odt0"

class StdOutListener(StreamListener):
	"""docstring fos StdOutListener"""
	def on_data(self,data):
		decoded = json.loads(data)
		print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
		#print (data)
		return True
	def on_error(self,status):
		print (status)

if __name__ == '__main__':
	l=StdOutListener()
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream=Stream(auth,l)
	stream.filter(track=['python','javascript','ruby'])