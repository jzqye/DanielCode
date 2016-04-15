import collections
import re
text = raw_input("Insert your text:")
split = re.split('\W+',text)
counter = collections.Counter(split)
wordfind = raw_input("Which word would you like to find?")
if wordfind.islower(): 
	text = text.lower()
	split = re.split('\W+',text)
	counter = collections.Counter(split)
	if counter[wordfind] == 0:
		print("Sorry, your word was not found.")
	elif wordfind.islower(): 
		text = text.lower()
		print ("Found It! '" + wordfind + "' occurs " + str(counter[wordfind]) + " times")
if wordfind.isupper():
		print ("Found It! '" + wordfind + "' occurs " + str(counter[wordfind]) + " times")
elif not wordfind.islower() and not wordfind.isupper():
		print ("Found It! '" + wordfind + "' occurs " + str(counter[wordfind]) + " times")