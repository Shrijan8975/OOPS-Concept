from emp import Emp

class Programmer(Emp):
    #Parameterized Constructor
    def __init__(self,id=0, nm="newEmp", sal=25000,eh=0,cph=0):
        print("I'm Programmer constructor...")
        super().__init__(id,nm,sal)
        self.extraHr = eh
        self.costPerHr =cph
        
    def displayProg(self):
        super().displayEmp()
        print("Extra Hours: {0}".format(self.extraHr))
        print("Cost Per Hour: {0}".format(self.costPerHr))
   
'''
p1= Programmer(222,"Amol",88000,75,500)
#p1.displayEmp()
p1.displayProg()
'''