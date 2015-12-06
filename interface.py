import os
import extBlkFeat
def home():
	os.system("dialog --backtitle 'by @iamprerit' --title 'Twitter Sentiment Analysis' --shadow --msgbox 'Press OK to proceed' 7 30")
	os.system("dialog --backtitle 'by @iamprerit' --title 'Twitter Sentiment Analysis' --shadow --msgbox 'sampleTweets.csv would be used for traing set' 7 30 ")
	os.system("dialog --backtitle 'by @iamprerit' --title 'Twitter Sentiment Analysis' --shadow --inputbox 'Enter file name containing test tweets:' 7 30 2>answer1.txt")
	os.system("dialog --backtitle 'by @iamprerit' --title 'Twitter Sentiment Analysis' --shadow --nook --msgbox 'Program in progress...please wait' 7 30")
	f=open('answer1.txt')
	filename=f.readline()
	f.close()
	extBlkFeat.extBlk(filename)
	os.system("dialog --backtitle 'by @iamprerit' --title 'Twitter Sentiment Analysis' --shadow --msgbox 'Your sentiment results are in the file finalResults.txt' 7 30")
home()
