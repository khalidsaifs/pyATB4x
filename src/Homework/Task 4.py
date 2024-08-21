### Task #4


# - Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
import math

R = int(input("Enter the radius value ="))
print(R)
print(f"{math.pi:0.2f}")
area=(math.pi * (R ** 2))
print(f"{area:.2f}")
