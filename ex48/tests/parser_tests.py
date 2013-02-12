from nose.tools import *
from bin import parser

word_list = [('alpha', 'letter_a'), ('charlie', 'letter_c')]

def test_peek():
	assert_equal(parser.peek(word_list), 'alpha')
	result = parser.peek(word_list)
	assert_equal(result, 'alpha')
	

	
