states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'Califronia': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '_' * 10
print "NY State has: ", cities['NY']
print "OR States has: ", cities['OR']

print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print '_' * 10
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city