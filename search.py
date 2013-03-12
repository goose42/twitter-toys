from twitter_search import twitter_search
from BeautifulSoup import BeautifulSoup

search = twitter_search()

for i in range (1,16):
  search.search_to_file("arsenal",str(i),"output.txt" )


