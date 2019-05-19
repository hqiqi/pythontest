class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    def __eq__(self, other):
        if not isinstance(other, Item):
            return False

        a = self.name == other.name
        b = self.weight == other.weight
        return a and b


cat_1 = Item('Cat', 5)
cat_2 = Item('Cat', 5)

print(cat_1.__eq__(cat_2))
print(cat_1 == cat_2)
