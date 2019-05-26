class Room:
	def __init__(self, name):
		"""TODO: Initialises a room. Do not change the function signature (line 2)."""
		self.name = name

	def get_name(self):
		"""TODO: Returns the room's name."""
		return self.name

	def get_short_desc(self):
		"""TODO: Returns a string containing a short description of the room. This description changes based on whether or not a relevant quest has been completed in this room.
		
		If there are no quests that are relevant to this room, this should return: 'There is nothing in this room.' """
		self.quest.
		return "desc"

	def get_quest_action(self):
		"""TODO: If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		...

	def set_quest(self, q):
		"""TODO: Sets a new quest for this room."""
		self.quest = Quest(q)

	def get_quest(self):
		"""TODO: Returns a Quest object that can be completed in this room."""
		...
		
	def set_path(self, dir, dest):
		"""TODO: Creates an path leading from this room to another."""
		...

	def draw(self):
		"""TODO: Creates a drawing depicting the exits in each room."""
		a = 11
		while a>=1:
        	if a == 11 or a == 1:
    			if a == 5:
    					if self.
        		print("+",end="")
        		i = inp
        while i > 1:
            print("--",end="")
            i-=1
        	print("+")
        	a-=1
    	else:
        	print("|",end="")
        	i = inp
        	while i > 1:
            	print("  ",end="")
            	i-=1
        		print("|")
        		a-=1

	def move(self, dir):
		"""TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		...
	def find_room_by_name(name):
		if name == self.name
		return self