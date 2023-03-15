class Emp:
    #Parameterized Constructor
    def __init__(self,id=0,nm="newEmp",sal=25000):
        self.eid = id
        self.name = nm
        self.salary = sal
    
    def setData(self):
     self.eid = int(input("Enter Emp Id: "))
     self.name = input("Enter Name: ")
     self.salary = float(input("Enter Salary: "))

    def getData(self):
        print("Eid: {0}".format(self.eid))
        print("Name: {0}".format(self.name))
        print("Salary: {0}".format(self.salary))
       

e1 = Emp(101,'Mangesh',80000)
print("--------------------------------")
e1.getData()
print("--------------------------------")

e2 = Emp()
print("--------------------------------")
e2.getData()
print("--------------------------------")

e3 = Emp()
print("--------------------------------")
e3.getData()
print("--------------------------------")

print("--------------------------------")
e1.getData()
print("--------------------------------")
