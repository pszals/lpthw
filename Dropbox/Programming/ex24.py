print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Defines function 'secret_formula' with one variable that can be inputed
def secret_formula(started):
# Defines variable 'jell_beans' as variable 'started' times 500
	jelly_beans = started * 500
# Defines variable 'jars' as variable 'jelly_beans' over 1000
	jars = jelly_beans / 1000
# Defines variable 'crates' as variable 'jars' over 100
	crates = jars / 100
# Calculates three numbers in a list that correspond to the three
# variables indented in 'secret_formula()'
	return jelly_beans, jars, crates
	
# Defines the variable 'start_point'
start_point = 10000
# Similar to 'argv' this defines three variable that will correspond 
# to the three numbers that come out of the 'secret_formula()'
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
# Calls on the variables given above that now have numerical values from
# the 'secret_formula'
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# Directly uses the 3 numbers that come out of the 'secret_formula'
# and inputs them into the given format characters
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)