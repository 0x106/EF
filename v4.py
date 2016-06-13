# version 4.0 EF Final Round Jordan Campbell

from subprocess import call
import sys
import numpy as np
import re
import matplotlib.pyplot as plt

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
	word = re.sub('[().",\],\[\d+\':!@#$%^&*]', '', word)
	# print word
	if len(word) > 0.0:
		try:
			corpus[word] += 1.0
		except:
			corpus[word] = 1.0

words = input_text.split()
for word in words:
	word = re.sub('[().",\],\[\d+\':!@#$%^&*]', '', word)
	if len(word) > 0.0:
		try:
			query[word] += 1.0
		except:
			query[word] = 1.0

# query terms and their significance
sig = []
for key in query:
	sig.append([key, float(query[key]) / float(corpus[key]), float(corpus[key])])# * float(corpus[key])  ])
sig = sorted(sig, key=lambda x: -x[1])


if False:
	values = []
	for item in sig:
		values.append(item[1])
		if item[1] < 10.0:
			print item

	if False:
		plt.plot(values)
		plt.show()

# 3. conduct searches on each significant term
# to provide a bit of variety we randomly take N terms above a given significance threshold.
# terms are chosen according to the 'probability' they are significant

N = 5
K = 0.15

terms = []
while(len(terms) < N):
	u, idx = np.random.rand(), int(np.random.rand() * len(sig))
	if u < sig[idx][1] and u > K and sig[idx][0]:
		terms.append(sig[idx]) 

print '------------------------'

for item in terms:
	print item[0], '\t', item[1]

# go back and find the sentences the top terms came from
# input_text = input_file.read().lower()
# print input_text
text = input_text.split('.')

sentences = []

for s in text:
	words = s.split()
	for i,word in enumerate(words):
		words[i] = re.sub('[().",\],\[\d+\':!@#$%^&*]', '', word)
	sentences.append("")
	for w in words:
		sentences[-1] += w + " "
	print '-->', sentences[-1]

for item in terms:
	for s in sentences:
		if item[0] in s:
			print item[0], '-->', s


# 4. Extract html for top links

# 5. compare terms to returned links

# 6. take the most relevant

# 