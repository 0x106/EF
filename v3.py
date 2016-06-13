from subprocess import call
import sys
import numpy as np
import re

# results = call(["googler", "bonsai", ">", "/Users/jordancampbell/Desktop/EF/output_file.txt"])

misc_characters = ['[', ']', '.', '"', "'"]

input_file = open('/Users/jordancampbell/Desktop/EF/baduk_input_file.txt')
corpus_file = open('/Users/jordancampbell/Desktop/EF/corpus.txt')
output_file = open('/Users/jordancampbell/Desktop/EF/output_file.txt')

input_text = input_file.read().lower()
corpus_text = corpus_file.read().lower()

corpus = {}
words = corpus_text.split()
for word in words:
	word = re.sub('[().",\],\[\d+\']', '', word)
	try:
		corpus[word]+=1.0
	except:
		corpus[word]=1.0

# for key in corpus:
# 	print key, '\t', corpus[key], '\t', np.log(float(corpus[key]))

words = input_text.split()
doc = {}
for word in words:
	word = re.sub('[().",\],\[\d+\']', '', word)
	try:
		doc[word]+=1.0
	except:
		doc[word]=1.0

tfidf = []

for key in doc:

	tfidf.append([key, float(doc[key]), float(corpus[key])])# * float(corpus[key])  ])

	# print key, '\t\t', doc[key], '\t\t', corpus[key], '\t\t', float(doc[key]) / np.log(float(corpus[key]))

tfidf = sorted(tfidf, key=lambda x: -x[1])

for item in tfidf:
	# if item[1] > 0 and item[1] < 10.:
	print item

# text = output_file.read()
# data = [text[i] for i in range(len(text))]

# links = []

# for i in range(len(data)):
# 	if data[i:i+4] == ['h', 't', 't', 'p']:
# 		idx = i-1
# 		links.append("")
# 		while data[idx] != '[':
# 			links[-1] += str(data[idx])
# 			idx += 1

# links[0] = links[0][1:]

# for l in links:
	# print l



