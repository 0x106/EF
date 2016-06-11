import numpy as np


sentences = []
sentences.append("This is a sentence about Hilary Clinton")
sentences.append("Donald Trump thinks that Hilary Clinton is silly")
sentences.append("I disagree with Donald Trump, I think he is bad for America.")
sentences.append("I would love to be lucky enough to join Entrepreneur First!")

N = min([len(s) for s in sentences])

print N

sentences = [s[:N] for s in sentences]

data = np.zeros((len(sentences), N))
for i, s in enumerate(sentences):
	for k, w in enumerate(s):
		data[i][k] = ord(w)


