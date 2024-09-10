class Login():
    #Attributes
    #Constructor
    def __init__(self,ui,pw):
        self.Ui=Ui
        self.pw=pw
    #Behaviour
    def login_info(self):
        if(Ui =="Saif" and pw =="saif4424"):
            print("Assalamualikum")
        elif(Ui !="Saif" and pw=="saif4424"):
            print("wrong Ui")
        elif(Ui =="Saif" and pw!="saif4424"):
            print("wrong Ui")
        else:
            print("Allah hafiz")

Ui=input("Enter the user id\n")
pw=input("Enter the password\n")

login=Login(Ui,pw)
login.login_info()
