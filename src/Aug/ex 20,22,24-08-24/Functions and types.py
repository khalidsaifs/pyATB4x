'''
Funtions:Funtion in python is a organised  and resuable block of code used to perform specific tasks.
funtion is formed by two parts
1. defining the funtion using def
2. calling the function

FUNTIONS are two types such as
1. built in:
Eg: print, max, sum, insert,etc

2. User_defined functions: These functions are created as per the requists.

There are four types such as

1. No return type and no argument:



def Greet():
    print("Assalmualikum")


Greet()

2. No return type with the argument:
'


def Greet(name):
    print("Assalamulaikum", name)


Greet("saifulla")


3.No return type with a user defined argument



def Greet(name1="Ashraff", name2="shabbu"):
    print("Assalamualikum", name2, name1)


Greet("Saif", "Shammu")


4. Return type with an argument

n1=int(input("Enter the value\n"))
n2=int(input("Enter the value\n"))

def sum(n1,n2):
    n1+n2
    return

l=sum(2,3)
print(l)

*arg FUnciotn: It is used for performing unlimited arguments.


Function source :It is used to perform outer function and inner function:
'''

def outer_funtion():
    print("Entering the inner function loops ")
    def inner_function():
        print("inner function")


    def inner_function2():
        print("inner function2")

    inner_function()
    inner_function2()

outer_funtion()