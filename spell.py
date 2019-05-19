class Spell:
	def __init__(self, name, school, level, cast_limit, effect):
		# Some instance variables, we expect as arguments.
		self.name = name
		self.school = school

		# Need to check if level is an int in range [0, 9].
		if not isinstance(level, int):
			raise TypeError("Invalid level specified.")
			# The spec says ValueError, but TypeError is a better one to raise here.

		if level < 0 or level > 9:
			raise ValueError("Invalid level specified.")

		self.level = level
		self.cast_limit = cast_limit
		self.effect = effect

		# The `casts` instance variable is derived from `cast_limit`.
		self.casts = self.cast_limit

	# ===== Getter Methods =====
	def get_name(self):
		return self.name

	def get_school(self):
		return self.school

	def get_level(self):
		return self.level

	def get_cast_limit(self):
		return self.cast_limit

	def get_effect(self):
		return self.effect

	def get_casts_left(self):
		return self.casts

	# ===== Other Methods =====
	def cast(self):
		if self.casts <= 0:
			print("Can't cast '{}' any more today.".format(self.name))
			return

		print("Casting '{}'...".format(self.name))
		self.casts -= 1
		print(self.effect + '\n')
		print("You can cast '{}' {} more time(s) today.".format(self.name, self.casts))

	def recharge(self):
		# Just need to reset `self.casts` to maximum.
		self.casts = self.cast_limit