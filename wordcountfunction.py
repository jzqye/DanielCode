import collections
import re
def findWord(text,wordFind):
	split = re.split('\W+',text)
	counter = collections.Counter(split)
	if wordFind.islower(): 
		text = text.lower()
		split = re.split('\W+',text)
		counter = collections.Counter(split)
		if counter[wordFind] == 0:
			print("Sorry, your word was not found.")
		elif wordFind.islower(): 
			text = text.lower()
			print ("Found It! '" + wordFind + "' occurs " + str(counter[wordFind]) + " times")
	if wordFind.isupper():
		print ("Found It! '" + wordFind + "' occurs " + str(counter[wordFind]) + " times")
	elif not wordFind.islower() and not wordFind.isupper():
		print ("Found It! '" + wordFind + "' occurs " + str(counter[wordFind]) + " times")
#TEST 1
text1 = "It's been nearly two years since Superman's (Henry Cavill) colossal battle with Zod (Michael Shannon) devastated the city of Metropolis. The loss of life and collateral damage left many feeling angry and helpless, including crime-fighting billionaire Bruce Wayne (Ben Affleck). Convinced that Superman is now a threat to humanity, Batman embarks on a personal vendetta to end his reign on Earth, while the conniving Lex Luthor (Jesse Eisenberg) launches his own crusade against the Man of Steel."
wordFind1 = "Superman"
findWord(text1, wordFind1)
#TEST 2
text2 = "We shouldn't have got the red card, it was totally unfair. It is not easy to play against Barcelona in the Champions League. We know it is really dangerous if they go out in the quarter-finals. We have to play against everyone and everything. We know it will be really difficult to go through but I think we are still alive. It is possible."
wordFind2 = "we"
findWord(text2, wordFind2)
#TEST 3
text3 = "The cataclysm that occurred at the end of the Cretaceous Period doomed many species, not just the dinosaurs. All the material hurled upwards would have darkened the sky and cooled the planet for months on end. But even as it took life away, the event also opened up new opportunities for those species that survived. And the expedition team wants to know if the impact zone itself became a life cradle."
wordFind3 = "youtube"
findWord(text3, wordFind3)