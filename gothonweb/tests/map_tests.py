from nose.tools import *
from bin.map import *

def test_room():
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. There's a
				door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
	
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
	assert_equal(START.go('N'), generic_death)
	assert_equal(START.go('n'), generic_death)
	assert_equal(START.go('y'), laser_weapon_armory)
	assert_equal(START.go('Y'), laser_weapon_armory)
	assert_equal(laser_weapon_armory.go('*'), generic_death)
	assert_equal(laser_weapon_armory.go('7'), the_bridge)
	assert_equal(the_bridge.go('Y'), escape_pod)
	assert_equal(the_bridge.go('y'), escape_pod)
	assert_equal(the_bridge.go('*'), generic_death)
	assert_equal(generic_death.go('Y'), central_corridor)
	assert_equal(generic_death.go('y'), central_corridor)
	assert_equal(generic_death.go('*'), exit)