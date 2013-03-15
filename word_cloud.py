#make a word could from a text file.
import re

import Image
import ImageDraw
import ImageFont
from collections import OrderedDict
import random
import time

regex1 = re.compile(r"[a-zA-Z0-9]*")
regex2 = re.compile(r"http:\/\/*")


words_to_ignore = ["all","is", "an", "at", "on","the", "and","but", "his","her","a","to","for"]

word_counter = {}
filtered_word_counter = {}
filename = raw_input("give us a txt file to scan: ")
with open (filename) as f:
  lines = f.readlines()
  
for line in lines:
  text = line.split()
  for word in text:
    if re.match(regex1,word) and not(re.match(regex2,word)):
      word_low = word.lower()
      if (word_low not in words_to_ignore) and (len(word_low)> 3):
        if word_counter.has_key(word_low):
          word_counter[word_low] += 1
        else:
          word_counter[word_low] = 1

for item in word_counter:
  if word_counter[item] > 2:
    filtered_word_counter[item] = word_counter[item]
    
ordered_word_count = OrderedDict(sorted(filtered_word_counter.items(), key=lambda x: x[1]))    


largest_size = ordered_word_count[next(reversed (ordered_word_count))]


img_slate = Image.new("RGB",(1300,500),"white")
draw =  ImageDraw.Draw(img_slate)
for i in range (0,150):
  word_to_print = next(reversed (ordered_word_count))
  x = random.randint(-600,600)
  y = random.randint(-200,200)
  frac = ordered_word_count[word_to_print]/float(largest_size)
  ordered_word_count.pop(next(reversed (ordered_word_count)))
  font_to_use = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf",int(150*frac)) #font type and size
  draw.text((650+x/2,250+y/2),word_to_print, font=font_to_use, fill="hsl(%d" % random.randint(0, 255) + ", 80%, 50%)")

timestamp = str(int(time.time()))
print "Files saved to output"+timestamp+".PNG"
img_slate.save("output"+timestamp+".PNG", "PNG")   
