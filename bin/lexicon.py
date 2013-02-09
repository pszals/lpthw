WORD_TYPES = {

"direction" : ['north', 'south', 'east'],
"verb" : ['go', 'kill', 'eat'],
"stop" : ['the', 'in', 'of'],
"noun" : ['bear', 'princess']

}

# inverts dictionary

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

def scan(sentence):
	tokens = []
	for word in sentence.split()
		
		try:
			word_type = VOCABULARY[word]
		
		except KeyError:
			
			try:
				value = int(word)
			
			except ValueError:
				tokens.append(('error', word))
			
			else:
				tokens.append(('int', value))
		
		else:
			tokens.append((word_tpye, word))
	
	return tokens
