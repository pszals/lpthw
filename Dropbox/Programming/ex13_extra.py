from sys import argv
# argv is an Argument variable. An Argument is something typed into the command line
# by the user.
script, hair, eyes = argv

hair = raw_input("What color is your hair? ")
eyes = raw_input("What color are your eyes? ")
print "The script is: ", script
print "So your hair is %s and your eyes are %s" % (hair, eyes)