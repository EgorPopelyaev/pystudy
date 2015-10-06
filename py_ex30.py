people = 20
cats = 30
dogs = 20

if people < cats:
	print "Too many cats!"	
elif people > cats:
	print "Not many ctas!"
else:
	print "We can't decide"
	
if people < dogs:
	print "The world is drooled on!"
elif people > dogs:
	print "The world is dry!"
else:
	print "We still can't decide"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
else:
	print "People are less than or equal to dogs."
