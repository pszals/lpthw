print "How old are you?",
# input() is similar, but the inputted term is treated as code and therefore has
# security problems, so it is best avoided by using raw_input()
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you are %s old, %s tall and %s heavy." % (
	age, height, weight)
	
print "How much money do you want to make?",
money = raw_input()
print "When does the cannon go off at Culver?",
cannon = raw_input()

print "So you will earn %s per year but still have to wake up every day at %s." % (
	money, cannon)