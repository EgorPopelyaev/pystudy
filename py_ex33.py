from sys import argv

scriptName, limit, incr = argv

numbers = []

def whileLoop(incriment, maxLimit):
	i = 0
	while i < maxLimit:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += incr
		print "Number now: ", numbers
		print "At the bottom i is %d" % i
	
whileLoop(incr, limit)	
	
print "The numbers: "

for num in numbers:
	print num