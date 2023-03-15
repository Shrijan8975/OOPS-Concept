#from <filename> import <classname> 
from emp import Emp

allEmp = {}
ch =0

while(ch !=7):
    print('''
        1. Add Emp
        2. Show All Emp
        3. Delete Emp on the basis of Emp Id
        4. Search Emp on the basis of EmpId
        7. Exit
    ''')

    ch = int(input("Enter your choice: "))
    if(ch == 1):
        name = input("Enter Emp name: ")
        sal = float(input("Enter Emp salary: "))
        e = Emp(name,sal)
        allEmp[e.eid] = e
    elif(ch == 2):
        #print(allEmp)
        for employee in allEmp.values():
            print("--------------------------------------------------")
            employee.getData()
    elif(ch == 3):
        empId = int(input("Enter Emp Id to be deleted: "))
        if(empId in allEmp):
            allEmp.pop(empId)
            print(empId, " is deleted..")
        else:
            print(empId, "is not present..")
    elif(ch == 4):
        empId = int(input("Enter Emp Id to be searhed: "))
        if(empId in allEmp):
            print(empId, " is found..")
            p = allEmp[empId]
            p.getData()
        else:
            print(empId, "is not present..")