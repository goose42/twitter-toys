from twitter_search import twitter_search
from BeautifulSoup import BeautifulSoup

search = twitter_search()

result = search.return_map_search("arsenal", "1")

for tweet in result:
  tweet_t = BeautifulSoup(tweet["text"]) 
  print "***",tweet_t, "\n"
