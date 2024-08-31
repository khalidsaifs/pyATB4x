# Class and Object Assignment
#
#
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee():
    # class is a user defined function,  which defines the attributes and behaviour of the object.
    # Attribute :through which class it is identifed.
    name =None
    age = None
    phone_number = None
    address = None
    eid = None

    #Constructor= It is called atomatically while running the programme. It is used to assign the values of the variables.
    #It is denoted by def__init__(self, Attribute variables):

    def __init__(self,name, age, phone_number,address,eid):
        self.name=name
        self.age=age
        self.phone_number=phone_number
        self.address=address
        self.eid =eid

    #Behaviour: What the attributes can do.
    #In behaviour self means current, self is mandatory argument used in every behaviour.
    def walk(self):
        print("who is walking\n", self.name  , self.age , self.phone_number , self.address , self.eid, sep="_" )

    def talk(self):
        print("who is talking\n", self.name, self.age, self.phone_number, self.address, self.eid, sep="_")
# Object = Object is rela time entity, instances of the class.
#class_ref =Class name()

n = input("Enter the employee name\n")
a = input("Enter the employee age\n")
p = input("Enter the employee phone number\n")
ad = input("Enter the employee address\n")
e = input("Enter the employee eid\n")

n2 = input("Enter the employee name\n")
a2 = input("Enter the employee age\n")
p2 = input("Enter the employee phone number\n")
ad2 = input("Enter the employee address\n")
e2 = input("Enter the employee eid\n")

employee1 =Employee(n,a,p,ad,e)
print(employee1)
employee1.walk()
employee1.talk()

employee2 =Employee(n2,a2,p2,ad2,e2)
print(employee2)
employee1.walk()
employee1.talk()