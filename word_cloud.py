#make a word could from a text file.
import re

regex = re.compile("[a-zA-Z]*")

word_counter = {}
with open ("output.txt") as f:
  lines = f.readlines()
  
for line in lines:
  text = line.split()
  for word in text:
    if re.match(regex,word):
      if word_counter.has_key(word):
        word_counter[word] += 1
      else:
        word_counter[word] = 1

print word_counter
