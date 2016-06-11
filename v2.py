import numpy as np

##
## The point of this program is to demonstrate that we can find
## the similarity between sentences.
##
## 1. Given a bunch of input sentences find the HSIC value between each
## 2. Query an input sentence from the user and return the closest match


# this is the kernel function that computes the feature space
# representation
def rbf(_x, _y, _cov):
	z = _x-_y
	q = np.dot(z.T, np.dot(_cov,z))
	return np.exp(-q)


# This is the function that actually computes the similarity between two sentences
def HSIC(_X, _Y, _cov, _H):
	N = _X.shape[0]
	K, L, KH, KL = np.zeros((N,N)), np.zeros((N,N)), np.zeros((N,N)), np.zeros((N,N))

	for i in range(N):
		for k in range(N):
			K[i,k] = rbf(_X[i], _X[k], _cov[0])
			L[i,k] = rbf(_Y[i], _Y[k], _cov[1])

	KH = np.dot(K, _H)
	LH = np.dot(L, _H)

	return ((1. / (N*N)) * np.trace(np.dot(KH, LH))) / np.sqrt(((1. / (N*N)) * np.trace(np.dot(KH, KH))) * ((1. / (N*N)) * np.trace(np.dot(LH, LH))))


sentences = []
sentences.append("This is a sentence about Hilary Clinton")
sentences.append("Donald Trump thinks that Hilary Clinton is silly")
sentences.append("I disagree with Donald Trump, I think he is bad for America.")
sentences.append("I would love to be lucky enough to join Entrepreneur First!")

# find the length of the shortest sentence
# At the moment the HSIC only works on identical length inputs - focus of major research!
N = min([len(s) for s in sentences])
M = len(sentences)

# truncate each sentence
sentences = [s[:N] for s in sentences]

# convert each sentence into its 'numbers' representation
data = np.zeros((len(sentences), N))
for i, s in enumerate(sentences):
	for k, w in enumerate(s):
		data[i][k] = ord(w)

# initialise everything we need for the HSIC
H = np.zeros((N,N))
for i in range(N):
	for k in range(N):
		H[i,k] = 0. - (1./N)
	H[i,i] = 1. - (1./N)

cov = [np.cov(data[i,:]) for i in range(M)]

for i in range(M):
	print sentences[i]
	for k in range(M):
		print i, k, HSIC(data[i,:], data[k,:], [cov[i], cov[k]], H)












