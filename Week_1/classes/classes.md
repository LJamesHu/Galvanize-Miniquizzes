## Classes and Inheritance

We'd like to create a class stucture for points in the cartesian plane (x, y points).

Here's how we should be able to use it:

    ```python
    p1 = Point(9, 2)
    p2 = Point(5, 5)
    print "distance:", p1.distance(p2)  # -> 5
    ```

1. Create a `Point` class which takes two values and stores them as instance variables (probably called `x` and `y`).

    You should be able to create points like this:

    ```python
    p1 = Point(9, 2)
    p2 = Point(5, 5)
    ```
    ```python
    class Point(object):

        def __init__(self, x, y):
            self.x = x
            self.y = y
    ```

2. Implement the `distance` class method. It should take another point and compute the euclidean distance between the two points.

    You should be able to use the distance method like this:

    ```python
    print "distance:", p1.distance(p2)  # <- 5
    ```
    ```python
    def distance(self, p2):
        return (((p2.x - self.x) ** 2) + ((p2.y - self.y) ** 2)) ** (0.5)
    ```

3. Implement a `Triangle` class which has three instance variables, one for each of the three points.

    Here's how you should create a triangle:

    ```python
    p3 = Point(2, 1)
    triangle = Triangle(p1, p2, p3)
    ```
    ```python
    class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    ```

4. Implement the `perimeter` method which gets the distances between each pair of points and adds together the three variables.

    To get the perimeter:

    ```python
    print "perimeter of triangle:", triangle.perimeter()  # <- 17.071
    ```
    ```python
    def perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)
    ```

5. **EXTRA CREDIT:** Write an `is_line` method for the `Triangle` class which returns `True` if all three points are in the same line (in which case it's a degenerate triangle).
