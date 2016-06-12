from subprocess import call
import sys

# results = call(["googler", "bonsai", ">", "/Users/jordancampbell/Desktop/EF/output_file.txt"])

misc_characters = ['[', ']', '.', '"', "'"]

input_file = open('/Users/jordancampbell/Desktop/EF/baduk_input_file.txt')
output_file = open('/Users/jordancampbell/Desktop/EF/output_file.txt')

input_text = input_file.read()

words = input_text.split()

for word in words:
	print word





text = output_file.read()
data = [text[i] for i in range(len(text))]

links = []

for i in range(len(data)):
	if data[i:i+4] == ['h', 't', 't', 'p']:
		idx = i-1
		links.append("")
		while data[idx] != '[':
			links[-1] += str(data[idx])
			idx += 1

links[0] = links[0][1:]

# for l in links:
	# print l



