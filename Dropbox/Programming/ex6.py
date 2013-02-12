# Defines variable x as a phrase, inserts a number inside of phrase via format character %d, 
# which can be used for numbers but not text
x = "There are %d types of people." % 10
# Defines variable binary
binary = "binary"
# Defines variable do_not as a contraction
do_not = "don't"
# Defines variable y as phrase with two format characters,
# then lists them to the right using open parentheses, variable, separating comma,
# second variable, closed parentheses 
y = "Those who know %s and those who %s." % (binary, do_not)
# Prints previously defined variable "x"
print x
# Prints previously defined variable "y"
print y
# Prints phrase string exactly x, which includes single quotation
print "I said: %r." % x
# Prints phrase string y
print "I also said: '%s'." % y
# Defines new variable 'hilarious' as False
hilarious = False
# Defines new variable as a string with a format character %r, print exactly this
joke_evaluation = "Isn't that joke so funny?! %r"
# Prints variable, defines variable hilarious as that which will substitute for the %r
# format character in string
print joke_evaluation % hilarious
# Defines new string variable
w = "This is the left side of..."
# Defines new string variable
e = "a string with a right side."
# Prints two strings, combining them with a plus 
print w + e
