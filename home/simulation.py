from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys

def read_paths(source):
	"""Returns a list of lists according to the specifications in a config file, (source).

	source contains path specifications of the form:
	origin > direction > destination.

	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""

	# TODO
	fi_le= open(source,"r")
	paths = fi_le.read()
	try:
		for path_taken in paths:
			path_taken = source.replace(" ","").split(">")
			origin = Room(path_taken[0])
			direction = path_taken[1]
			destination = path_taken[2]
		return None
	except:
		print("")
	pass

def create_rooms(paths):
	
	"""Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""

	# TODO

	fi_le= open(paths,"r")
	rooms = fi_le.read()
	for room in rooms:
		path_taken = source.replace(" ","").split(">")
		origin = Room(path_taken[0])
		direction = path_taken[1]
		destination = path_taken[2]
	return None
	

def generate_items(source):
	"""Returns a list of items according to the specifications in a config file, (source).

	source contains item specifications of the form:
	item name | shortname | skill bonus | will bonus
	"""

	# TODO
	
	fi_le= open(source,"r")
	items = fi_le.read()
	try:
	for item in items:
		its = item.split("|").strip
		it = Item(its[0],its[1],its[3],its[4]) 
	return None
	except:
	pass


def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""
	
	# TODO
	fi_le= open(source,"r")
	items = fi_le.read()
	for item in items:
		its = item.split("|").strip
		quest = Quest(its[0],its[1],its[3],its[4])
	return None

	
	
	pass


# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.


# TODO: Receive commands from standard input and act appropriately.
main():
	inp = input(">>>")
	if inp == "help":
		print("SHIT")