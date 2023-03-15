from admin import Admin
from prog import Programmer
from salesMgr import SalesMgr

print("---------------------------------------------")
a1= Admin(333,"Aditya",85000,7500)
a1.displayAdmin()
print("---------------------------------------------")

s1= SalesMgr(444,"Adarsh",88000,75000)
s1.displaySalesMgr()

print("---------------------------------------------")

p1= Programmer(222,"Amol",88000,75,500)
p1.displayProg()

print("---------------------------------------------")
