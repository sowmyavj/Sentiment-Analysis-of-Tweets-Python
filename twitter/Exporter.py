# -*- coding: utf-8 -*-
import sys,getopt,datetime,codecs
import re
from textblob import TextBlob

#if sys.version_info[0] < 3:
import getTweets


def main(argv):

	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return

	if len(argv) == 1 and argv[0] == '-h':
		f = open('exporter_help_text.txt', 'r')
		print f.read()
		f.close()

		return

	try:
		opts, args = getopt.getopt(argv, "", ("username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets", "maxtweets=", "output="))

		tweetCriteria = getTweets.manager.TweetCriteria()
		outputFileName = "_output_got.csv"

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg

			elif opt == '--since':
				tweetCriteria.since = arg

			elif opt == '--until':
				tweetCriteria.until = arg
				

			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg

			elif opt == '--toptweets':
				tweetCriteria.topTweets = True

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)
			
			elif opt == '--near':
				tweetCriteria.near = '"' + arg + '"'
			
			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--output':
				outputFileName = arg

		outputFileName = tweetCriteria.since + '_output_got.csv'
		outputFile = codecs.open(outputFileName, "w+", "utf-8")

		outputFile.write('Date,Hour,Minute,Tweet text,Polarity,Sentiment')
		print('Searching...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				cleaned_tweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",t.text).split())
				analysis=TextBlob(cleaned_tweet)
				if analysis.sentiment.polarity < 0:
					sentiment=-1
				elif analysis.sentiment.polarity > 0:
					sentiment=1
				else:
					sentiment=0
				#outputFile.write(('\n%s,"%s",%f,%s' % (t.date.strftime("%Y-%m-%d %H:%M"),cleaned_tweet,analysis.sentiment.polarity,sentiment)))
				#date_hour,date_min,sentiment,web_url,date,id
				#23,39,-1,https://www.nytimes.com/2017/03/01/learning/lesson-plans/401-prompts-for-argumentative-writing.html,3/1/2017,58b75b9c95d0e024902fd01f
				outputFile.write(('\n%s,%s,%s,"%s",%f,%s' % (t.date.strftime("%m/%d/%Y"),t.date.strftime("%H"),t.date.strftime("%M"),cleaned_tweet,analysis.sentiment.polarity,sentiment)))
				
			outputFile.flush();
			print('More %d saved on file...\n' % len(tweets))
		
		getTweets.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

	except arg:
		print('Arguments parser error, try -h' + arg)
	finally:
		outputFile.close()
		print('Done. Output file generated "%s".' % outputFileName)

if __name__ == '__main__':
	main(sys.argv[1:])
