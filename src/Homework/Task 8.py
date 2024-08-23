'''✅ Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.'''
l1=int(input("enter the length1 = \n"))
l2=int(input("enter the length2 = \n"))
l3=int(input("enter the length3 = \n"))
if(l1==l2==l3):
    print("It is a equilateral triangle.")
elif(l1==l2!=l3):
    print("it is a isosceles triangle")
elif(l1!=l3==l2):
    print("it is a isosceles triangle")
elif(l1==l3!=l2):
    print("it is a isosceles triangle")
elif(l1!=l3!=l2):
    print("It is a scalene triangle")



