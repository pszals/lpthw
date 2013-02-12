# Define variable "age" as a user input in response to text within quotes
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input ("How much do you weigh? ")
# Prints result of inputs into sentence by using percent and format character string
# open parentheses and separates variables by comma and space
print "So, you're %s old, %s tall and %s heavy." % (
	age, height, weight)