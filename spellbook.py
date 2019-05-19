class Spellbook:
	def __init__(self, material, capacity):
		self.material = material
		self.capacity = capacity
		# We need to keep track of the spells somehow, so let's use a list.
		self.spells = []
		# It will make our lives easier if we kept track of our total accumulated spell level, too.
		self.total_spell_level = 0

	def add_spell(self, spell):
		# Need to check if the spell can fit!
		if self.total_spell_level + spell.get_level() > self.capacity:
			raise ValueError("We're nearing the end of our power budget. You can't write '{}' into this spellbook.".format(spell.get_name()))

		# If it does, we update two instance variables:
		self.spells.append(spell)
		self.total_spell_level += spell.get_level()

	def cast_spell(self, name):
		# Time to search for a spell!
		i = 0
		while i < len(self.spells):
			if self.spells[i].get_name() == name:
				self.spells[i].cast()
				return				# End the function here if we have found an appropriate spell.
			i += 1

		# If we found no spells that match the name, we print this error message:
		print("There is no spell called '{}' here.".format(name))

	def cast_strongest(self):
		# Should probably check that our spell list is empty first.
		if len(self.spells) == 0:
			print("There are no spells in this spellbook.")
			return
		
		strongest = None
		i = 0
		while i < len(self.spells):
			# We should deal only with spells that can be cast!
			if self.spells[i].get_casts_left() > 0:
				if strongest == None:
					# First spell we encounter that can be cast becomes our strongest.
					strongest = self.spells[i]
				elif self.spells[i].get_level() >= strongest.get_level():
					# Otherwise, we compare spell levels.
					strongest = self.spells[i]

			i += 1

		if strongest == None:
			print("No more spells can be cast from this spellbook today.")
		else:
			strongest.cast()

	def cast_all(self):
		# Casts all the spells that can be cast in the spellbook.
		count = 0
		i = 0
		while i < len(self.spells):
			if self.spells[i].get_casts_left() > 0:
				self.spells[i].cast()
				count += 1
				print()
			i += 1

		print("Cast {} spells!".format(count))

	def recharge_all(self):
		# Recharges every spell in the book.
		i = 0
		while i < len(self.spells):
			self.spells[i].recharge()
			i += 1