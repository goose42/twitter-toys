from twitter_search import twitter_search
from BeautifulSoup import BeautifulSoup

search = twitter_search()

search_string = raw_input("what would you like to search for today? ")
output_file = raw_input("Give me a name of a file to output to:")

for i in range (1,16):
  search.search_to_file(search_string,str(i),output_file)


