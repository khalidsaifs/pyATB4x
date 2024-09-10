'''Inheritence: It is concpet of OOPs, in which the the attributes and classes are accuired from another class.
 It allws the class to inherit the attributes and behaviour from parent class.

 Types:
 single inheritence
 multi level inheritence
 multiple inheritence
 Hirerachical inheritence
 hybrid inheritence'''


# Single Inhertence:
#
# class Father:
#
#     key = "1Bhk"
#
#     def property(self):
#         print("fathers property is 1BHk")
#
# class Son(Father):
#     key = "2BHK"
#
#     def home(self):
#         print("sons property is 2 BHK")
#
#
# f = Father()
# s = Son()
# print(s.key)
# s.home()
# s.property()

# class Papa:
#     # doc = "3 bhk"
#     # money = "1lakh"
#     #
#     def __init__(self, doc, money):
#         self.doc = doc
#         self.money = money
#
#     def property(self):
#         print(f"fathers property is {self.doc} and {self.money} ")
#
#
# class Beta(Papa):
#
#     def __init__(self, savings):
#         self.savings = savings
#
#     def property_2(self):
#         print(f"The sons havinga proeprty of {self.savings}")
#
#
# p = Papa("3bhk", "25laks")
# b = Beta("10 lakhs")
#
# b.property_2()
# p.property()
# b.property()

# Multilevel Inheritence:

# class grand_father:
#
#     key = "1 bhk"
#
#     def home(self):
#         print("grand father has proper of 1 BHK")
#
# class Father(grand_father):
#
#     key2 = "2 bhk"
#
#     def home2(self):
#         print("father has aproperty of 2 bhk")
#
# class Son(Father):
#
#     car = "volks wagen"
#
#     def vehicle(self):
#         print("Son has a proerty of volks wagen car")
#
# gf = grand_father()
# f = Father()
# s = Son()
#
# s.home()
# s.home2()
# s.vehicle()
# f.home()
# f.home2()

# multiple inheritence:

# class father:
#
#     def fathers_money(self):
#         return 5
#
#     def home(self):
#         print("this is fathers home")
# class Mother:
#
#     def mothers_money(self):
#         return 3
#
#     def home(self):
#         print("this is mothers home")
# class Son(father,Mother):
#     pass
#
# class Son2(Mother, father):
#     pass
#
#
# S = Son()
# S2 = Son2()
# print(S.fathers_money())  '''MRO :Method reolution order'''
# print(S.mothers_money())
# S.home()
# S2.home()
# dimond problem {Interview question}
# as per the above like 119, it only prints the fathers home because in line 111 we have given father name first, so it gets the output depending on the
# whos name is first given.
# to know this more clrarly you can see the son2 result.It guve the result as{this is mothers home} becuase mothers name is given first.

# Hirerarical inheritence:

class Father:

    key = "1Bhk"

    def property(self):
        print("fathers property is 1BHk")

class son(Father):

    def property1(self):
        print("2BHK")

class son2(Father):

    def property(self):
        print("3bhk")

