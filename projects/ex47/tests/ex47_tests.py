from nose.tools import *
from ex47.game import Room

def test_room():
	gold = Room("GoldRoom", """This room has gold in it you can grab.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.path, {})

def test_room_path():
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
	
	assert_equals(start.go('west'), west)
	assert_equals(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
	
def test_room_grab_things():
		gold = Room("GoldRoom", """This room has gold in it you can grab.""")
		coins = Room("Coins", "Money")
		dark_room = Room('DarkRoom', "This room has nothing except darknes.")
		emptyness = Room("Emptyness", "Dark room is emty")
		
		gold.grab_things({'coins': coins})
		dark_room.grab_things({'emptyness': emptyness})
		
		assert_equals(gold.check_bag('coins'), coins)
		assert_equals(dark_room.check_bag('emptyness'), emptyness)