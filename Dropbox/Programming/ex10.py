tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
#Everything inside triple quotes gets printed
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
#BEL makes the bell noise, or error sound on a Mac
print "My friend the ASCII Bell (BEL) \a BEL\a\a\a"
#Backspace \b removes a space, but will not delete text if more \b's are included
print "My friend the Backspace (BS) \bBS\b\b2 2"
#Form Feed makes new page, but text is spaced over exactly where it is on the line prior
print "Whatever Formfeed is\f(FF)is for suckers\f(FF)"
#Linefeed puts text immediately after on a new line
print "Linefeed (I think this means new line) \n(LF)"
#Carriage return makes new line, not sure how it is different from Line Feed
print "Carriage return \rThis comes after the carriage return"
#\\ puts backslash into string
print "This is a backslash escape\\"
#Can't figure out how to make this print unicode for lowercase e with umlauts
print "How about a new character? \N&#203"

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i