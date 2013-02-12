print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Stand up tall with arms reaching high and back slowly, still facing the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	elif bear == "3":
		print "You manage to escape the dark room, but find yourself in a confusing passageway."
		print "There seems to be a secret door off to the left. What do you do?"
		print "1: Push secret door"
		print "2: Pull secret door"
		
		secret = raw_input("> ")

	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
		
	insanity = raw_input("> ")
		
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jellow.  Good job!"
	else: 
		print "The insanity rots your eyes into a pool of muck.  Good job!"
		
else:
	print "You stumble around and fall on a knife and die.  Good job!"

if secret == "1":
	print "The door won't budge. As you tap on it, you suddenly feel a weight in your pocket."
	print "You reach in and find a strange key. What do you do?"
	print "1. Try key in door"
	print "2. Put key in pocket and go out the way you came in."
	
	key = raw_input("> ")
	
	if key == "1":
		print "Seems not to fit into the door. The key might be worth something though, looks like gold."
		print "You leave the way you came in.  Good job!"
	elif key == "2":
		print "Smart choice. The key seemed delicate, and it might break inside the lock."
		print "If that happened you wouldn't be able to sell it for as much money."
	else: 
		print "A vampire comes out of the darkness and sucks your blood.  Good job!"
elif secret == "2":
	print "You can't push a rope, silly!  Good job!"

else:
	print "You stumble around and fall on a knife and die.  Good job!"
