from sys import exit
import random

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."

class Engine(object):
""" This class runs the game. The first function initializes the class so that
the class takes the variable scene_map. The second function sets the current
scene equal to the scene map (the parameter entered into Engine()) and calls
the function opening_scene from the Map() class. Next, a while loop is created
that puts a line between each scene. Every scene has the function enter()
followed by text and a call to action, thus the next scene name is determined
by what gets returned from the enter() function, namely, a key to the next
scene in the dictionary in the Map() class.
"""
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n -----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)		

class Death(Scene):
	
	def enter(self):
		print "You have died. Womp womp. Retry? Y/N."
		
		while True:
			retry = raw_input("> ")
			if retry == 'y' or (retry == 'Y'):
				return 'central_corridor'
			elif retry == 'n' or (retry == 'N'):
				exit()
			else:
				print "I don't understand that."
			
				
class CentralCorridor(Scene):
	
	def enter(self):
		print "You find yourself in the Central Corridor after having just"
		print "witnessed the murder of your best friend at the hands of a"
		print "slimy Gothon. You had quickly run away, fighting back tears,"
		print "only to run into another Gothon who is blocking your path."
		print "You know from your third grade Univers History class that"
		print "a Gothon's biggest weakness is its sense of humor. You decide"
		print "to tell it a corny joke. 'What's brown and sticky?'"
		print "You seem to have caught the Gothon by surprise. It contemplates"
		print "for a moment, then gives up. 'A stick!' you counter."
		print "\n"
		print "Was the joke funny? Y/N."
		
		while True:
			funny = raw_input("> ")
			if funny == 'y' or (funny == 'Y'):
				return 'laser_weapon_armory'
			elif funny == 'n' or (funny == 'N'):
				return 'death'
			else:
				"I don't understand that."

class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "You have reached the armory. In it you see a vaguely familiar"
		print "symbol. You recall learning about it in your fourth grade"
		print "particle physics class, but can't quite place it. 'Aha!' you"
		print "think to yourself. 'That symbol means radioactive!' A neutron"
		print "bomb? That might do the trick. But it's locked up - you must"
		print "guess the right number on the key pad to access it. Numbers"
		print "1-9. Choose the right number, quick!"
				
		while True:
			guess = int(raw_input("> "))
			code = random.randint(1, 9)
			
			if guess == code:
				return 'the_bridge'
			elif guess != code:
				return 'laser_weapon_armory'
			else:
				print "I don't understand that."

class TheBridge(Scene):
	
	def enter(self):
		print "You have reached the final staging area. This is where you must"
		print "plant the bomb in order to destroy all of the slimy Gothons who"
		print "brutally murdered your friends and families. In a moment of"
		print "hesitation though, you realize that the Gothons probably have"
		print "friends and family too. Do you really want to blow them all up?"
		print "Y/N?"
		
		while True:
			decision = raw_input("> ")
			
			if decision == "Y" or (decision == "y"):
				return 'escape_pod'
			elif decision == "N" or (decision == "n"):
				return 'death'
			else:
				print "I don't understand that"
				
class EscapePod(Scene):
	
	def enter(self):
		print "You enter the escape pod and feel relieved. You have barely"
		print "survived. You see a bright light as you look out the window"
		print "behind you. The Gothons are dead. All dead, at last!"
		print "A long journey lies ahead of you, but at least"
		print "you're alive. Congratulations. GAME OVER."
		
		exit()
		
# This class is a dictionary of the different scenes that functions as a game map
class Map(object):
""" This is the map of the game. It contains a dictionary with all of the
scenes from the game in it. The first function initializes the class with
start_scene so that it can take a parameter. The second function takes a
scene name and returns the corresponding class from the dictionary. The
third function calls the second function with whatever parameter was put
into the Map() class and returns it.
"""
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()