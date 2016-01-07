class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return (((p2.x - self.x) ** 2) + ((p2.y - self.y) ** 2)) ** (0.5)


class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)


p1 = Point(9, 2)
p2 = Point(5, 5)
print "distance:", p1.distance(p2)
p3 = Point(2, 1)
triangle = Triangle(p1, p2, p3)
print "perimeter of triangle:", triangle.perimeter()