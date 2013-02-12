from nose.tools import *
from bin import parser

word_list = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

def test_peek():
	assert_equal(parser.peek(word_list), 'a')
	result = parser.peek(word_list)
	assert_equal(result, 'a')
	

	
