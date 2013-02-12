# This is the reader for the file I just wrote with extra16.py
from sys import argv

script, filename = argv

print "This is the %s script and it is going to read the %s file!" % (
	script, filename)

target = open(filename)

print target.read()