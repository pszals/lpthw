def exponent(base, power):
	print "Calculating %s to the %s power:" % (base, power)
	return base ** power

print "This will calculate exponents, just give me the base and power"
print exponent(int(raw_input("Base: ")), int(raw_input("To the power of: ")))

def cube(cube_base):
	print "Calculating cube of %s " % (cube_base)
	return cube_base ** 3
	
print "This cubes a number, what number would you like to cube?"
print cube(int(raw_input("To be cubed: ")))