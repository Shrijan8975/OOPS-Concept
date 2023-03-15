
class Emp:
    #Parameterized Constructor
    def __init__(self,id=0, nm="newEmp",sal=25000):
        print("I'm Emp constructor...")
        self.eid = id
        self.ename = nm
        self.salary = sal
        
    def displayEmp(self):
        print("Eid: {0}".format(self.eid))
        print("Name: {0}".format(self.ename))
        print("Salary: {0}".format(self.salary))

'''
e1= Emp(111,"Priyal",90000)
e1.displayEmp()
'''