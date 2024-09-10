# polymorphism: It is a oops concept,
# It allows the object behaviour of different class can be treated as object of same super class.
# They can be achieved by two methods
# method Over riding
# method over loding

# method Over riding:
class shape:

    def area(self):
        print("Are of the shape")


class Rectangle(shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):

        print(f"The area of teh rectangle is{self.length * self.width}")
        super().area()
class circle(shape):

    def __init__(self,radius,):
        self.radius = radius

    def area(self):
        print(f"The area of the circle is{3.14*self.radius**2}")
        super().area()

r = Rectangle(2,3)
c = circle(2)
r.area()
c.area()

# using super(). for calling the parent function.
class shape:

    def area(self):
        print("Are of the shape")


class Rectangle(shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):

        print(f"The area of teh rectangle is{self.length * self.width}")
        super().area()
class circle(Rectangle):

    def __init__(self,radius,length,width):
        self.radius = radius
        self.length = length
        self.width = width

    def area(self):
        print(f"The area of the circle is{3.14*self.radius**2}")
        super().area()

r = Rectangle(2,3)
c = circle(2,2,3)
r.area()
c.area()


# method overloding:
# It is OOPs concpets,
# python doesnot support method over loding.

    def