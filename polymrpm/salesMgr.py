from emp import Emp

class SalesMgr(Emp):
    #Parameterized Constructor
    def __init__(self,id=0, nm="newEmp", sal=25000,comm =0):
        #print("I'm SalesMgr constructor...")
        super().__init__(id,nm,sal)
        self.commission = comm

    def displayDetails(self):
        super().displayDetails()
        print("Commission: {0}".format(self.commission))
        

'''
s1= SalesMgr(444,"Adarsh",88000,75000)
#s1.displayEmp()
s1.displaySalesMgr()
'''