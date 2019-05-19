class Box:
    def __init__(self):
        self.contents = []


    def add_item(self, item):
        self.contents.append(item)


    def get_weight(self):
        """Return the weight of the box (the total
        weight of all items in the box).
        """
        total = 0

        i = 0
        while i < len(self.contents):
            item = self.contents[i]
            total += item.weight
            i += 1

        return total


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# Some sample code that uses the Box and Item classes.
b = Box()
b.add_item(Item('Cat', 5))
b.add_item(Item('Nintendo Switch', 1))
b.add_item(Item('Potatoes', 2))

msg = 'The box weighs {} kg'.format(b.get_weight())
print(msg)  # The box weighs 8 kg
