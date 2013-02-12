# Creates class Map with parameter self and object
class Map(object):
# defines a variable as a list of scenes corresponding to a variety of Classes
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}
# Class Map has-a __init__ that takes self and start_scene parameters
	def __init__(self, start_scene):
# From self get the start_scene attribute and set it to start_scene
		self.start_scene = start_scene
# Class Map has-a next_scene function that takes self and scene_name parameters
	def next_scene(self, scene_name):
# Returns From class Map from scenes get the get function and call it with 
# paramaters self and scene_name
		return Map.scenes.get(scene_name)
# Class Map has-a opening_scene function that takes parameter self
	def opening_scene(self):
# Returns from self get the next_scene function and call it with the parameters self
# and start_scene
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()