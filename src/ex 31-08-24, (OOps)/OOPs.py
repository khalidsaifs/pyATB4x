#  Oops: Object Oriented Programming.It is methodlogy which uses the class and object concepts to design the programme.
#It is divded into class and Objects.
# Productivity is high
# used un Java and Python languages.

#Class: It is user defined function, which defines the attributes and behaviour of the object.
#Attributes: through which you are identified.
#Behaviour: what you can do.
#syntax:

#class (name):
    #Attributes


    #Behavious




# Objects : It is a real time entity. Instances of the class.
#The attributes and behaviour of the class can be accesed using the object.

#Example:

class Dog(): #class name is always starts with capital letter.
    #Attribute : Through which you are identified.
    name = None
    age = None
    bread =None # In attributes we never give the value of variables because,
                # the value will be common for all the classes.
                #Attribute variables are local variables. We can use unlimited attributes.


#Constructor = It is called atomatically when running the programme.
    # It is used to initialize the values of the variable in the attributes.
    # We can it for unlimited attributes.
    # it is defined by --init--(self).
    #syntax def --init--(self,name,age,sex):
        #self.name=name
        #slef.age = age
        #self.sex = sex
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed


    #behaviour: What the class does.

    def sleep(self): #in class the behaviour function always have the argument self. but we can neglect that and it is not a first argument.
        print("who is sleeping" +self.name+str(self.age)+self.breed)

    def barking(self,name):
        print("who is barking" +self.name+str(self.age)+self.breed)

  #  def running(self, name):
   #      return "it is running"

#Object: It is real entity, instances of the class. the attributes and behviour of the class are assesed by using object.
#object_ref = class name()
# dog = Dog()
# dog.name = "Mow"
# print(dog.name)
# dog.barking(dog.name)
# dog.running(name= dog.name)
dog =Dog("mow",10,"lulu")
print(dog.name)
dog.sleep()
dog.barking("dow")
