class Pet:
    def __init__(self, name, age, species, trained):
        if (not isinstance(name, str) or
            not isinstance(age, int) or
            not isinstance(species, str) or
            not isinstance(trained, bool)):
            # At least one argument has an incorrect type
            raise TypeError

        if (len(name) == 0 or
            age <= 0 or
            len(species) == 0):
            # At least one argument has an incorrect value
            raise ValueError

        self.name = name
        self.nicknames = []  # instead of a list, a set would be more suitable here
        self.age = age
        self.species = species
        self.house_trained = trained


    def has_nickname(self, name):
        i = 0
        while i < len(self.nicknames):
            nick = self.nicknames[i]

            if nick == name:
                return True
            i += 1

        return False


    def add_nickname(self, name):
        if not isinstance(name, str):
            raise TypeError

        if len(name) == 0:
            raise ValueError

        if not self.has_nickname(name):
            self.nicknames.append(name)


p1.add_nickname('Donut')   # `p1` refers to a Pet object
p1.add_nickname('Dodo')    # Pet `p1` now has nicknames 'Donut' and 'Dodo'
p1.add_nickname('')        # raises an exception!

p1.has_nickname('Donut')   # True
p1.has_nickname('Dodo')    # True
p1.has_nickname('Dondon')  # False
