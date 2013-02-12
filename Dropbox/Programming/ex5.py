name = 'Philip A. Szalwinski'
age = 26 # not a lie
height = 74 # inches
weight = 160 # lbs
eyes = 'Blue'
teeth = 'White'
hair ='Brown'
toothpaste = 'Crest'
# % takes the variable on the right, named above, and inserts it.
# %s works for strings or numbers
# %d only works for numbers
# %r prints the whole variable named, including surrounding punctuation,
# like '' and "" --> "print this no matter what"
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "He uses %r toothpaste." % toothpaste

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)