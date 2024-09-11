# excpetion: It is an error that occur during the execution of a programme and disturb the normal flow of programe.
#  it can be cause during any type of problem such as type error or invalid key error.
# it casued during the execution of a problem such as arthematic error, value error, atribute error, etc
# ERROR: It is caused, if there is any mistake in the code, such as syntax error.
#  below example gives a clear idea

'''# print(a)  =  NameError: name 'a' is not defined


a = int(input("nter num1"))
b = int(input("nter num2"))
c = a/b  # there are chances of ZeroDivisionError: division by zero, if it is divisble by zero

print(c) #There are chances of ValueError: invalid literal for int() with base 10: 'ghy', if the str is used instead of int.

# we can except this errors by following syntax.
# start
# try
# except
# finish

# example
print("start")

try:
    a = int(input("nter num1"))
    b = int(input("nter num2"))
    c = a / b  # there are chances of ZeroDivisionError: division by zero, if it is divisble by zero

   # print(c)   # There are chances of ValueError: invalid literal for int() with base 10: 'ghy', if the str is used instead of int.
except ZeroDivisionError as e:
    print("please check the input")

except ValueError as ve:
    print("please enter teh integer value, you have enetered string")
else:
    print(f"the result is {c} ")
finally:
    print("The code is executed")
'''
# try, except,finally
import os
# try:
#     file= open("OOPs.py",'r')
#
# except Exception as e: # if we dont know the Exception type we can use the father varible that is "Exception".
#     print("file not found, please enter the valid file name")
# else:
#     print(file.read())
# finally:
#     print("close")

'''Cuatom Exception: this type of exception is used when we dont have standered type of exception.'''

class MyownException(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 1100
withdraw = int(input("enter the amount"))
if (withdraw > balance):
    print("insufficient balance")

else:
    print(f"please take cash and balance is {balance-withdraw}")