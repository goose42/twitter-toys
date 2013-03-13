#make a word could from a text file.
import re

regex1 = re.compile(r"[a-zA-Z0-9]*")
regex2 = re.compile(r"http:\/\/*")



word_counter = {}
with open ("output.txt") as f:
  lines = f.readlines()
  
for line in lines:
  text = line.split()
  for word in text:
    if re.match(regex1,word) and not(re.match(regex2,word)):
      if word_counter.has_key(word):
        word_counter[word] += 1
      else:
        word_counter[word] = 1

for item in word_counter:
  if word_counter[item] > 1:
    print item,word_counter[item]
