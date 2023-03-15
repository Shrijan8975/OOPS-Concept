from emp import Emp

class Admin(Emp):
    #Parameterized Constructor
    def __init__(self,id=0, nm="newEmp", sal=25000,incen =0):
        print("I'm Admin constructor...")
        super().__init__(id,nm,sal)
        self.incentive = incen

    def displayAdmin(self):
        super().displayEmp()
        print("Incentive: {0}".format(self.incentive))
        

'''
p1= Admin(333,"Aditya",85000,7500)
#p1.displayEmp()
p1.displayAdmin()
'''