### Task #7
'''
✅ Leap Year Checker:
Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.'''

y=int(input("Enter the year : \n"))
if(y%4 ==0 and y%100 !=0 ) or (y%400 ==0) :
    print(f"The {y} is a leap year")
else:
    print(f" The {y} is not a leap year")

'''
elif(y%400 ==0):
    print("This is a leap year")
elif(y%100 !=0):
    print("This is a leap year")'''

#elif(y/100):
 #   print("This is not a leap year")
