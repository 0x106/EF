import numpy as np

text = "Less is known about Aristophanes than about his plays. In fact, his plays are the main source of information about him. It was conventional in Old Comedy for the Chorus to speak on behalf of the author during an address called the 'parabasis' and thus some biographical facts can be found there. However, these facts relate almost entirely to his career as a dramatist and the plays contain few clear and unambiguous clues about his personal beliefs or his private life.[13] He was a comic poet in an age when it was conventional for a poet to assume the role of 'teacher' (didaskalos), and though this specifically referred to his training of the Chorus in rehearsal, it also covered his relationship with the audience as a commentator on significant issues.[14]. Aristophanes claimed to be writing for a clever and discerning audience,[15] yet he also declared that 'other times' would judge the audience according to its reception of his plays.[16] He sometimes boasts of his originality as a dramatist[17] yet his plays consistently espouse opposition to radical new influences in Athenian society. He caricatured leading figures in the arts (notably Euripides, whose influence on his own work however he once begrudgingly acknowledged),[18] in politics (especially the populist Cleon), and in philosophy/religion (where Socrates was the most obvious target). Such caricatures seem to imply that Aristophanes was an old-fashioned conservative, yet that view of him leads to contradictions.[19]"
# text = "Mitt Romney argued on Friday that Donald Trump's rhetoric could make racist and misogynistc sentiments more permissible in America."

sentences = text.split('.')
ignore = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'America']
people = ['Hilary', 'Clinton', 'Bernie', 'Sanders']

names = {}

for s in sentences:

	sentence = s.split()
	sentence[0] = sentence[0].lower()

	for word in sentence:

		if word[0].isupper() and not word in ignore:

			try:
				names[word]+=1.0
			except:
				names[word]=1.0
			# names.append(word)


print names

M = len(names)

ex = 0
for k in names.keys():
    h = names[k]/M
    ex -= np.sum(h*np.log(h))

print ex







