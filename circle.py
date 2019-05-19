class Circle:
    PI = 3.1415

    def get_wiki_page():
        print('A circle is a shape with only one side.')

    def __init__(self, rad):
        self.radius = rad

    def get_area(self):
        # Circle area: pi * (r^2)
        return Circle.PI * (self.radius ** 2)


# How Circle attributes and methods can be accessed
Circle.PI
Circle.get_wiki_page()

c1 = Circle(2)
c1.radius
c1.get_area()

c2 = Circle(5)
c3 = Circle(4)
