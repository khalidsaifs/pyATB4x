'''Encapsulation: the binding or wrapping of the data members using methods (public, protccted and private)
Public: data members can be used in the entire programme.
Protected: data members can be accesed with the class and sub class.
Private: data members can be accesed within the class.
'''


class Bank:
    # # public Varible
    # acc_num = None
    # # protected variable
    # _password = "Saif"
    # # private variable
    # __password1 = "Saifulla"

    def __init__(self, acc_num, _password, __password, balance):
        self.acc_num = acc_num
        self._password = _password
        self.__password = __password
        self.balance = balance

    def show_balance(self):
        print(self.balance)

    def balance_after_deposite(self, deposite):
        self.balance = self.balance + deposite
        print(self.balance)


    def show_info(self, auth):
        if auth == True:
            print(self.acc_num, self._password, self.__password)
        else:
            print(self.acc_num)


hdfc = Bank(124345, "Saif", "Saifulla", 300)

print(hdfc.show_balance())
print(hdfc.balance_after_deposite(200))
print(hdfc.acc_num)
print(hdfc._password)
# print(hdfc.__password)
hdfc.show_info(True)
