# I can't get this for loop to count by increments. Is it possible?

def for_count(variable):
	
	i = 0
	numbers = []
	
	for i in range(variable):
		print "At the top, i is %d" % i
		numbers.append(i)
		
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom, i is %d" % i
		
	print "The numbers: "
	
	for num in numbers:
		print num
		
	
	
