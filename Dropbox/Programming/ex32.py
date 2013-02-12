# This defines a variable as a list of numbers, surrounded by bracket characters
the_count = [1, 2, 3, 4, 5]
# A list can consist of strings as well
fruits = ['apples', 'oranges', 'pears', 'apricots']
# A list can be a mix of numbers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# Basically, "for a given number within this list:"
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it                             
for x in change:
	print "I got %r" % x

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Elements was: %d" % i