from sys import exit

def dead(why):
	print why, "\n\tGAME OVER."
	exit(0)

def start():
	"""This is the start of the game"""
	print """
You find yourself standing in front of an old creaky house. The windows are
boarded up, spindly trees lean inwardly toward the house as if they are
beckoned inside. You feel yourself being drawn to the front door.
Do you:
1. Go inside.2
2. Run away screaming like a little girl.
"""
	
	start = raw_input("> ")
	
	if start == "1":
		great_hall()
	else:
		print """
A strange force leaves you with no choice. You enter the house despite your
better judgement.
"""
		great_hall()

def great_hall():
	"""This is the main area of the house"""
	print """
You enter the house and are surprised by the interior. You stand in a great
hall that is nothing like what you saw on the outside. The place seems frozen
in time, as if under some magical "stop time" spell. You look around and see a
few places you	might like to explore. Who knows, there could be some treasure
here to sell in your shop. There is a massive staircase straight in front of
you, a closet to your right, around the staircase seems to be some space, and
to the left -- what is that? A fully stocked bar?? 

What direction do you go?
"""
	
	while True:
		choice = raw_input("> ")
		
		try:
			result = direction[choice]
		
		except KeyError:
			print "I don't understand that."
		
		else:
			result()

start()

def great_hall_return():
	print """GREAT HALL RETURN. The staircase is the one part of the house that is not under the
spell. It crumbles underneath your weight and you fall back to where you started.
"""
	"""Back in the main area of the house"""
	
	print """
There is a massive staircase straight in front of you, a closet to your right,
around the staircase seems to a crawlspace, and to the left is the wet bar.

What direction do you go?
"""
		
	while True:
		choice = raw_input("> ")
		
	try:
		result = direction[choice]
		
	except KeyError:
		print "I don't understand that."
		
	else:
		result()
	
	
	
def closet():
	"""This is the closet with a vampire in it"""
	print """
You approach the closet and notice that the door handle is broken.
"""
	
	open_closet = raw_input("> ")
	
	if "open" in open_closet:
		print """
You see an open coffin with a vampire inside.
"""
		vampire()

	elif vampire == "back":
		great_hall_return()

	else:
		print """
You can't get up the nerves to open the door.
"""
		great_hall_return()

def vampire():
	"""This vampire will wake up and take you somewhere"""
	print """
The vampire is sleeping. You walk up to it and can hear it breathe. You can
poke it, or try and suck its blood.
"""
		
	while True:
		vampire_action = raw_input("> ")
		
		if vampire_action == "poke":
			vampire_awakens()
		
		elif vampire_action == "suck":
			print """
You realize that's not how vampirism works.
"""
			vampire()
			
		elif vampire_action == "blood":
			print """You realize that's not how vampirism works.
"""
			vampire()
		
		elif vampire_action == "back":
			great_hall_return()
		
		else:
			print "I don't understand that."

def vampire_awakens():
	print "Were you thinking about drinking my blood?"
	
	response = raw_input("> ")
	
	if "no" in response:
		print "Just kidding, I should be drinking YOUR blood!"
		print "But instead, I'll take you to my secret stash."
		crawlspace()
	
	if "yes" in response:
		print "Weirdo. Everyone knows you can't drink a vampire's blood!"
		print "But because I like you, I'll show you something cool."
		crawlspace()
	
	else:
		vampire_awakens()

def bar():
	print "Sweet! There's top-shelf gin, vodka, rum, and scotch!"
	
	while True:
		drink = raw_input("> ")
		
		if drink == "gin" or (drink == "vodka") or (drink == "rum"):
			print "Everything was poisoned except the scotch! RESTART."
			great_hall_return()
		
		elif drink == "scotch":
			print """
			Scotchy scotch scotch. In-to my belly... In a drunken
			stupor you find yourself leaning against the wall underneath the
			staircase.
			"""
			crawlspace()
		
		elif drink == "back":
			great_hall_return()
	
		else:
			print "I don't understand that."


def crawlspace():
	print "You approach the closet underneath the stairs and hear...hooting?"
	closet = raw_input("> ")
	
	if "open" or "enter" in closet:
		print """
You enter a room and immediately find the source of that odd hooting noise.
It's Hedgewig! And Harry Potter! The two of you drink some scotch and practice
your magic and live happily ever after. GAME OVER.
"""
		exit()
	
	elif "back" in closet:
		great_hall_return()
	
	else:
		crawlspace()

direction = {
	'straight': great_hall_return,
	'left': bar,
	'right': closet,
	'around': crawlspace
	}



			
