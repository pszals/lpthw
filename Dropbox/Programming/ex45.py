from sys import exit

class Scene(object):

	def enter(self):
		print "This scene is not yet configured."

class Runner(object):
	""" 
This class runs the game. The first function initializes the class so that
the class takes the variable scene_map. The second function sets the current
scene equal to the scene map (the parameter entered into Runner()) and calls
the function opening_scene from the Map() class. Next, a while loop is created
that puts a line between each scene. Every scene has the function enter()
followed by text and a call to action, thus the next scene name is determined
by what gets returned from the enter() function in the current scene, namely, 
a key to the next scene in the dictionary in the Map() class.
"""

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class OldHouse(Scene):
	
	def enter(self):
		print """
You find yourself standing in front of an old creaky house. The windows are
boarded up, spindly trees lean inwardly toward the house as if they are
beckoned inside. You feel yourself being drawn to the front door.
Do you:
1. Go inside.
2. Run away screaming like a little girl.
"""
		start = raw_input("> ")
	
		if start == "1":
			return 'great_hall'
		else:
			print """
A strange force leaves you with no choice. You enter the house despite your
better judgement.
"""
			return 'great_hall'

class GreatHall(Scene):

	def enter(self):
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
			direction = {
				'straight': 'staircase',
				'left': 'bar',
				'right': 'closet',
				'around': 'under_stairs'
	}
			try:
				result = direction[choice]
		
			except KeyError:
				print "I don't understand that."
		
			else:
				return result
			
class Staircase(Scene):
	
	def enter(self):
		print """
The staircase is the one part of the house that is not under the spell. It
crumbles underneath your weight and you fall to your death. Luckily you
reincarnate back at the front of the old house.
"""
		return 'old_house'
		
class Bar(Scene):

	def enter(self):
		print "Sweet! There's top-shelf gin, vodka, rum, and...SCOTCH!"
		print "Pick your poison!"
	
		while True:
			drink = raw_input("> ")
		
			if drink == "gin" or (drink == "vodka") or (drink == "rum"):
				print "\nEverything was poisoned except the scotch! RESTART."
				return 'old_house'
		
			elif drink == "scotch":
				print """
Scotchy scotch scotch. In-to my belly... In a drunken stupor you find yourself
leaning against the wall underneath the staircase.
"""
				return 'under_stairs'
		
			elif drink == "back":
				return 'great_hall'
	
			else:
				print "I don't understand that."
		
class UnderStairs(Scene):

	def enter(self):
		print "You approach the closet underneath the stairs and hear..."
		print "hooting?"
	
		closet = raw_input("> ")
	
		if "open" or "enter" in closet:
			return 'hp'
		
		elif "back" in closet:
			return 'great_hall'
		
		else:
			print "I don't understand that."
			
class Hp(Scene):
	
	def enter(self):
		print """
You enter a room and immediately find the source of that odd hooting noise.
It's Hedgewig! And Harry Potter! The three of you drink some scotch and
practice your magic and live happily ever after. GAME OVER.
"""
		exit()
			
class Closet(Scene):

	def enter(self):
		"""This is the closet with a vampire in it"""
		print """
You approach the closet and notice that the door handle is broken.
"""
	
		open_closet = raw_input("> ")
	
		if "open" in open_closet:
			print """\n----------\n
You see an open coffin with a vampire inside.
"""
			return 'vampire'
		
		elif "push" in open_closet:
			print """\n----------\n
You see an open coffin with a vampire inside.
"""
			return 'vampire'

		elif open_closet == "back":
			return 'great_hall'

		else:
			print """
You can't get up the nerves to open the door.
"""
			return 'great_hall'
			
class Vampire(Scene):
	
	def enter(self):
		"""This vampire will wake up and take you somewhere"""
		print """
The vampire is sleeping. You walk up to it and can hear it breathe. You can
poke it, or try and suck its blood.
"""
		
		while True:
			vampire_action = raw_input("> ")
		
			if vampire_action == "poke":
				return 'coffin'
		
			elif vampire_action == "suck":
				print """
You realize that's not how vampirism works.
"""
				return 'coffin'
			
			elif vampire_action == "blood":
				print """You realize that's not how vampirism works.
"""
				return 'coffin'
		
			elif vampire_action == "back":
				return 'great_hall'
		
			else:
				print "I don't understand that."
			
class Coffin(Scene):
	
	def enter(self):
		print "The vampire awakens."
		print '"Were you thinking about drinking my blood?"'
	
		response = raw_input("> ")
	
		if "no" in response:
			print """\n----------
Just kidding, I should be drinking YOUR blood! But instead, I'll take you to
my secret stash.
"""
			return 'under_stairs'
	
		if "yes" in response:
			print """\n----------Weirdo. Everyone knows you can't drink a
vampire's blood! But because I like you, I'll show you something cool.
"""
			return 'under_stairs'
	
		else:
			return 'coffin'
		
class Map(object):
	
	scenes = {
			'old_house': OldHouse(),
			'great_hall': GreatHall(),
			'staircase': Staircase(),
			'bar': Bar(),
			'closet': Closet(),
			'hp': Hp(),
			'under_stairs': UnderStairs(),
			'coffin': Coffin(),
			'vampire': Vampire()
		}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)

first_map = Map('old_house')
game = Runner(first_map)
game.play()

		