from emp import Emp

class Admin(Emp):
    #Parameterized Constructor
    def __init__(self,id=0, nm="newEmp", sal=25000,incen =0):
        #print("I'm Admin constructor...")
        super().__init__(id,nm,sal)
        self.incentive = incen

    def displayDetails(self):
        super().displayDetails()
        print("Incentive: {0}".format(self.incentive))

    def __str__(self):
        data = super().__str__()
        data += "\nIncentive: " +str(self.incentive)
        return data 

    def calSal(self):
        #return super().calSal() + self.incentive
        return self.salary + self.incentive

'''
p1= Admin(333,"Aditya",85000,7500)
#p1.displayEmp()
p1.displayAdmin()
'''