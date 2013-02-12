# create a mapping of state to abbreviation
states = {
'Texas': 'TX',
'Illinois': 'IL',
'Indiana': 'IN',
'Tennessee': 'TN',
'California': 'CA'
}

# create a basic set of states and some cities in them
cities = {
'TX': 'Houston',
'TX': 'Austin',
'IL': 'Chicago',
'IN': 'Culver',
'TN': 'Nashville',
'CA': 'San Francisco'
}

# print out some cities
print "Texas has: ", cities['TX']
print "Illinois has: ", cities['IL']

# print some states
print "Texas' abbreviation is: ", states['Texas']
print "Illinois' abbreviation is: ", states['Illinois']

# do it by using the state then cities dict
print "Indiana has: ", cities[states['Indiana']]
print "Tennessee has: ", cities[states['Tennessee']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s." % (state, abbrev)
	
# print every city in each
print '-' * 10
for state, city in cities.items():
	print "%s state has %s." % (state, city)
	
# now do both at the same time
"""For each state and abbreviation print the state, abbreviation, and city that
corresponds to each abbreviation"""
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has %s" % (
		state, abbrev, cities[abbrev])
		
print '-' * 10
state = states.get('Illinois', None)

if not state:
	print "Sorry, no state."

if state:
	print "State: ", state
