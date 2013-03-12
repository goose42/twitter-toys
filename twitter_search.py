import urllib
import json
from BeautifulSoup import BeautifulSoup
import math

class twitter_search:
  def __init__(self):
    self.count=0
    self.file_handle = "output.txt"
    self.twitter_url = "http://search.twitter.com/search.json?q="
    self.res_pp = 100
    self.lang = "en"
  
  def set_lang(self, lang):
    self.lang = lang
  
  def set_rpp(self, num):
    self.res_pp = num
  
  def search_internal(self,query,page_num):
    return_json = urllib.urlopen(self.twitter_url+query+"&rpp="+str(self.res_pp) 
    +"&page="+page_num+"&lang="+self.lang+"&result_type=recent")
    return_map = json.loads(return_json.read())
    for tweet in return_map["results"]: #results gives us a list of dictionaries
      tweet_text = BeautifulSoup(tweet["text"])
      print "*", tweet_text.string.encode('utf-8'),"\n"
      self.count+=1
  
  def gimmie(self, query, number):
    pages = int(math.ceil(number/100.0))
    if pages < 16:
      pages +=1
    else:
      pages = 16
    for i in range(1,pages):
      if i == (pages-1):
        self.res_pp = number%100
      self.search_internal(query,str(i))
  
  def search_return_map(self,query,page_num):
    return_json = urllib.urlopen(self.twitter_url+query+"&rpp="+str(self.res_pp) 
    +"&page="+page_num+"&lang="+self.lang+"&result_type=recent")
    return_map = json.loads(return_json.read())
    return return_map["results"]
  
  def search_to_file(self,query, page_num,file_name):
    return_json = urllib.urlopen(self.twitter_url+query+"&rpp="+str(self.res_pp) 
    +"&page="+page_num+"&lang="+self.lang+"&result_type=recent")
    return_map = json.loads(return_json.read())
    f = open(file_name,"w")
    for tweet in return_map["results"]:
      tweet_text = BeautifulSoup(tweet["text"])
      print "**"+tweet_text.string
      f.write(tweet_text.string.encode('utf-8'))
      f.write("\n")
    f.close()
