from sys import argv

script, value1, value2 = argv

def add(val1, val2):
	return int(val1) + int(val2)
	
def dif(val1, val2):
	int_val1 = int(val1)
	int_val2 = int(val2)
	if (int_val1 > int_val2):
		return int_val1 - int_val2
	else: 
		return int_val2 - int_val1

addition = add(value1, value2)
print "The sum of input values: %d" % addition

difference = dif(value1, value2)
print "The difference between input values: %d" % difference 
