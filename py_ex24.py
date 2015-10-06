print "Let's practice everything."
print "You\'d need to know \'boutescapes with \\ taht do \n new lines and  tabs."

poem = """
\t The lovely world
with logic so firmly planted 
cannot discern \n needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print
print "--------------------"
print poem
print "--------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
startPoint = 10000
beans, jars, crates = secret_formula(startPoint)

print "With a start point of: %d" % startPoint
print "We'd have  %d beans, %d jars, %d crates." % (beans, jars, crates)

startPoint = startPoint / 10

print "We can also do that this way."
print "We'd have %d beans, %d jars, %d cartes." % secret_formula(startPoint)