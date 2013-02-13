from nose.tools import *
from bin import parser

word_list = [('alpha', 'letter_a'), ('charlie', 'letter_c')]

def test_peek():
	word_list = [('alpha', 'letter_a'), ('charlie', 'letter_c')]
	assert_equal(parser.peek(word_list), 'alpha')
	result = parser.peek(word_list)
	assert_equal(result, 'alpha')
	
def test_match():
	word_list = [('alpha', 'letter_a'), ('charlie', 'letter_c')]
	assert_equal(parser.match(word_list, 'alpha'), ('alpha', 'letter_a'))
	
def test_skip():
	word_list = [('alpha', 'letter_a'), ('charlie', 'letter_c')]
	assert_equal(parser.skip(word_list, 'alpha'), None)
	
def test_parse_verb():
	word_list = [('verb', 'go'), ('stop', 'the')]
	exception = [('noun', 'noun')]
	assert_equal(parser.parse_verb(word_list), ('verb', 'go'))
	assert_raises(parser.ParserError, parser.parse_verb, exception)
	

def test_parse_object():
	exception = [('verb', 'verb')]
	
	direction = [('direction', 'north')]
	noun = [('noun', 'epee')]
	assert_equal(parser.parse_object(direction), ('direction', 'north'))
	assert_equal(parser.parse_object(noun), ('noun', 'epee'))
	assert_raises(parser.ParserError, parser.parse_object, exception)
	
def test_parse_subject():
	subject = ('noun', 'bear')
	verb = ('verb', 'eats')
	obj = ('noun', 'honey')
	
	word_list = [('verb', 'eats'), ('noun', 'honey')]
	result = parser.parse_subject(word_list, subject)
	assert_equal(result.subject, 'bear')
	assert_equal(result.verb, 'eats')
	assert_equal(result.object, 'honey')
	
def test_parse_sentence():
	# Tests the skip function
	stop = [('stop', 'the')]
	assert_raises(parser.ParserError, parser.parse_sentence, stop)
	
	word_list = [('verb', 'eats'), ('noun', 'honey')]
	result = parser.parse_sentence(word_list)
	assert_equal(result.subject, 'player')
	assert_equal(result.verb, 'eats')
	assert_equal(result.object, 'honey')

	