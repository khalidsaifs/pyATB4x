# file handling is like reand or write the file in the python.
# open('filename','mode')
# It is simple to handle
# file = open('OOps.py','r')
# content =file.read()
# print(content)
# import os
#
# full_path = os.path.join('src/Sep/ex 31-08-24, (OOps)/OOps 2.py','OOps.py')
# file = open(full_path,'r')
# content = file.read()
# print(content)

# with open('OOPs.py','r')as file:
#     file.read("hello")

# we can acess the excel file data. using pandas
import pandas as pd
df = pd.read_csv("testdata.csv")
print(df)