
## Prerequisites
This package assumes using Python 2.x. 

Expected package dependencies are listed in the "requirements.txt" file for PIP, you need to run the following command to get dependencies:
```
pip install -r requirements.txt
```

## Components
- **Tweet:** Model class to give some informations about a specific tweet.
  - id (str)
  - permalink (str)
  - username (str)
  - text (str)
  - date (date)
  - retweets (int)
  - favorites (int)
  - mentions (str)
  - hashtags (str)
  - geo (str)

- **TweetManager:** A manager class to help getting tweets in **Tweet**'s model.
  - getTweets (**TwitterCriteria**): Return the list of tweets retrieved by using an instance of **TwitterCriteria**. 

- **TwitterCriteria:** A collection of search parameters to be used together with **TweetManager**.
  - setUsername (str): An optional specific username from a twitter account. Without "@".
  - setSince (str. "yyyy-mm-dd"): A lower bound date to restrict search.
  - setUntil (str. "yyyy-mm-dd"): An upper bound date to restrist search.
  - setQuerySearch (str): A query text to be matched.
  - setTopTweets (bool): If True only the Top Tweets will be retrieved.
  - setNear(str): A reference location area from where tweets were generated.
  - setWithin (str): A distance radius from "near" location (e.g. 15mi).
  - setMaxTweets (int): The maximum number of tweets to be retrieved. If this number is unsetted or lower than 1 all possible tweets will be retrieved.
  
- **Main:** Examples of how to use.

- **Exporter:** Export tweets to a csv file named "output_got.csv".

## Examples of python usage
- Get tweets by username
``` python
	tweetCriteria = getTweets.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	tweet = getTweets.manager.TweetManager.getTweets(tweetCriteria)[0]
	  
    print tweet.text
```    
- Get tweets by query search
``` python
	tweetCriteria = getTweets.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
	tweet = getTweets.manager.TweetManager.getTweets(tweetCriteria)[0]
	  
    print tweet.text
```    
- Get tweets by username and bound dates
``` python
	tweetCriteria = getTweets.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	tweet = getTweets.manager.TweetManager.getTweets(tweetCriteria)[0]
	  
    print tweet.text
```
- Get the last 10 top tweets by username
``` python
	tweetCriteria = getTweets.manager.TweetCriteria().setUsername("barackobama").setTopTweets(True).setMaxTweets(10)
	# first one
	tweet = getTweets.manager.TweetManager.getTweets(tweetCriteria)[0]
	  
    print tweet.text
```

## Examples of command-line usage
- Get help use
```
    python Exporter.py -h
``` 
- Get tweets by username
```
    python Exporter.py --username "barackobama" --maxtweets 1
```    
- Get tweets by query search
```
    python Exporter.py --querysearch "europe refugees" --maxtweets 1
```    
- Get tweets by username and bound dates
```
    python Exporter.py --username "barackobama" --since 2015-09-10 --until 2015-09-12 --maxtweets 1
```
- Get the last 10 top tweets by username
```
    python Exporter.py --username "barackobama" --maxtweets 10 --toptweets
