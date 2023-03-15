from emp import Emp

class Programmer(Emp):
    #Parameterized Constructor
    def __init__(self,id=0, nm="newEmp", sal=25000,eh=0,cph=0):
        #print("I'm Programmer constructor...")
        super().__init__(id,nm,sal)
        self.extraHr = eh
        self.costPerHr =cph
        
    def displayDetails(self):
        super().displayDetails()
        print("Extra Hours: {0}".format(self.extraHr))
        print("Cost Per Hour: {0}".format(self.costPerHr))
        
    def __str__(self):
        data = super().__str__()
        data += "\nCost Per Hour: " +str(self.costPerHr)
        data += "\nExtra Hour: " +str(self.extraHr)
        return data

    
    def calSal(self):
        #return super().calSal() + (self.costPerHr * self.extraHr)
        return self.salary + (self.costPerHr * self.extraHr)
    

p1= Programmer(222,"Amol",88000,75,500)
#p1.displayEmp()
print(p1)