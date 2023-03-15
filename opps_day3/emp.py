
class Emp:
    #Static variable
    count = 100

    #Parameterized Constructor
    def __init__(self,nm="newEmp",sal=25000):
        Emp.count += 1
        self.eid = Emp.count
        self.ename = nm
        self.salary = sal
        
    def getData(self):
        print("Eid: {0}".format(self.eid))
        print("Name: {0}".format(self.ename))
        print("Salary: {0}".format(self.salary))
