from sys import exit

class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
central_corridor = Room("Central Corridor",
"""
You find yourself in the Central Corridor after having justwitnessed the murder
of your best friend at the hands of a slimy Gothon. You had quickly run away,
fighting back tears, only to run into another Gothon who is blocking your path.
You know from your third grade Univers History class that a Gothon's biggest 
weakness is its sense of humor. You decide to tell it a corny joke. 'What's 
brown and sticky?' You seem to have caught the Gothon by surprise. It 
contemplates for a moment, then gives up. 'A stick!' you counter.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You have reached the armory. In it you see a vaguely familiar symbol. You 
recall learning about it in your fourth grade particle physics class, but can't
quite place it. 'Aha!' you think to yourself. 'That symbol means radioactive!'
A neutron bomb? That might do the trick. But it's locked up - you must guess 
the right number on the key pad to access it. Numbers 1-9. Choose the right 
number, quick!
""")

the_bridge = Room("The Bridge",
"""
You have reached the final staging area. This is where you must plant the bomb
in order to destroy all of the slimy Gothons who brutally murdered your friends
and families. In a moment of hesitation though, you realize that the Gothons 
probably have friends and family too. Do you really want to blow them all up?
""")

escape_pod = Room("Escape Pod",
"""
You enter the escape pod and feel relieved. You have barely survived. You see a
bright light as you look out the window behind you. The Gothons are dead. All 
dead, at last! A long journey lies ahead of you, but at least you're alive. 
Congratulations. GAME OVER.
""")

generic_death = Room("death", "You have died. Womp womp.")

retry = Room("retry", "Retry? Y/N")

generic_death.add_paths({
	'Y': central_corridor,
	'y': central_corridor,
	'*': exit
})

the_bridge.add_paths({
	'Y': escape_pod,
	'y': escape_pod,
	'*': generic_death
})

laser_weapon_armory.add_paths({
	'7': the_bridge,
	'*': generic_death
})

central_corridor.add_paths({
	'Y': laser_weapon_armory,
	'y': laser_weapon_armory,
	'N': generic_death,
	'n': generic_death
})

START = central_corridor
START.go("Y")