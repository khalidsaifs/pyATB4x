# Abstraction: It is a oops concept.
# it is used to hide the inner details and show the only required area.
# we need to from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        print("start the car")
    @abstractmethod
    def stop(self):
        print("stop the car")
class Car(Vehicle):

    # def __init__(self,start, stop):
    #     self.start()
    #     self.stop()
    def start(self):
        print("start the car")


    def stop(self):
        print("stop the car")

    def drive(self):
        self.start()
        print("drive the car")
        self.stop()


c = Car()
c.drive()

# example 2:

class Testing:
    @abstractmethod
    def start(self):
        print("start")

    @abstractmethod
    def end(self):
        print("end")

class Test_case(Testing):
    def start(self):
        print("start")
    def end(self):
        print("end")
    def compile(self):
        self.start()
        print("the data is running")
        self.end()

tc1= Test_case()

tc1.compile()