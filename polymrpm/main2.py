from admin import Admin
from prog import Programmer
from salesMgr import SalesMgr

print("---------------------------------------------")
a1= Admin(333,"Aditya",85000,7500)
s1= SalesMgr(444,"Adarsh",88000,75000)
p1= Programmer(222,"Amol",88000,75,500)

'''
s1.displayDetails()
a1.displayDetails()
p1.displayDetails()

'''
allEmpList = [p1,s1,a1]

print("---------------------------------------------")

for e in allEmpList:
    #Polymorphic Statements
    e.displayDetails()
    print("---------------------------------------------")
