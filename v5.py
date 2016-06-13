## version 5.0


import re
import numpy as np

def sim(_words, _joint, _prior):
	result = 0.0

	for w1 in _words[0]:
		for w2 in _words[1]:
			phrase = w1 + w2
			try:
				result += float(joint[phrase] / prior[w1])
			except:
				result += 0.0

	# print len(_words[0]), len(_words[0])	

	return result / (len(_words[0])+len(_words[1]))

corpus_file = open('/Users/jordancampbell/Desktop/EF/baduk_input_file.txt')
corpus_text = corpus_file.read().lower()

joint, prior = {}, {}
words = corpus_text.split()
for idx, word in enumerate(words):
	words[idx] = re.sub('[().",\],\[\d+\':!@#$%^&*]', '', word)

for i in range(len(words)):

	try:
		prior[words[i]] += 1.0
	except:
		prior[words[i]]  = 1.0

	for k in range(len(words)):
		phrase = words[i] + words[k]

		if abs(i - k) < 80:
			try:
				joint[phrase] += 1.0
			except:
				joint[phrase]  = 1.0


query = []
query.append("her eyes are green")
query.append("its a race")
query.append("i enjoy growing bonsai")

for q1 in query:
	q1 = q1.split()
	for q2 in query:

		q2 = q2.split()

		likelihood = sim([q1, q2], joint, prior) / ((sim([q1, q1], joint, prior)*sim([q2, q2], joint, prior))+1.0)

		print likelihood



