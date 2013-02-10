dictionary = {

"direction" : ['north', 'south', 'east'],
"verb" : ['go', 'kill', 'eat'],
"stop" : ['the', 'in', 'of'],
"noun" : ['bear', 'princess'],
"car" : ['lambo', 'corvette', 'miata', 'fit', 'civic']

}

def scan(input):
	actions = []
	inverted_dictionary = (
	dict((word, word_type) for word_type, words in dictionary.items()
	for word in words)
	)
	
	for word in input.split():
		try:
			word_type = inverted_dictionary[word.lower()]
			
		except KeyError:
			
			try:
				value = int(word)
				
			except ValueError:
				actions.append( ('error', word) )
			
			else:
				actions.append( ('number', value) )
				
			
		else:
			actions.append( (word_type, word) )
				
	return actions