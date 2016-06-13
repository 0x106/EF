# version 4.0 EF Final Round Jordan Campbell

from subprocess import call
import sys
import numpy as np
import re

# 1. extract text from an article
input_file = open('/Users/jordancampbell/Desktop/EF/baduk_input_file.txt')
corpus_file = open('/Users/jordancampbell/Desktop/EF/corpus.txt')
output_file = open('/Users/jordancampbell/Desktop/EF/output_file.txt')

input_text = input_file.read().lower()
corpus_text = corpus_file.read().lower()

# 2. extract the significant words

#build corpus histogram
corpus, query = {}, {}
words = corpus_text.split()
for word in words:
	word = re.sub('[().",\],\[\d+\']', '', word)
	try:
		corpus[word]+=1.0
	except:
		corpus[word]=1.0

words = input_text.split()
for word in words:
	word = re.sub('[().",\],\[\d+\']', '', word)
	try:
		query[word]+=1.0
	except:
		query[word]=1.0

# query terms and their significance
sig = []
for key in query:
	sig.append([key, float(query[key]), float(corpus[key])])# * float(corpus[key])  ])
sig = sorted(sig, key=lambda x: -x[1])

for item in sig:
	print item


# 3. conduct searches on each significant term

# 4. Extract html for top links

# 5. compare terms to returned links

# 6. take the most relevant

