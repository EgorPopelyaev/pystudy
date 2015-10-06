def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
	print "You have %d cheeses!" % cheeseCount
	print "You have %d boxes of crackers!" % boxesOfCrackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
print "We can give the function numbersdirectly:"
cheeseAndCrackers(20, 30)

print "Or, we can use variables from our script:"
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers)

print "We can even d math inside too:"
cheeseAndCrackers(10 + 20, 5 + 6)

print "And we combine the two variables and math:"
cheeseAndCrackers(amountOfCheese + 10, amountOfCrackers + 69)

