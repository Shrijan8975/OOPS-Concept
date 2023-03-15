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
        5. Search Emp on the basis of Emp Name
        6. Edit Emp on the basis of EmpId
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
    elif(ch == 5):
        empName = input("Enter Emp Name to be searhed: ")
        for employee in allEmp.values():
            if(empName.lower() == employee.ename.lower()):
                print(empName, " is found..")
                employee.getData()
                break
            else:
                print(empName, "is not present..")
    elif(ch == 6):
        empId = int(input("Enter Emp Id to be searhed: "))
        if(empId in allEmp):
            ans = input("Do you wish to edit emp name(y/n) ?")
            if(ans.lower() == 'y'):
                empName = input("Enter Emp Name: ")
                allEmp[empId].ename  = empName        
            
            ans = input("Do you wish to edit emp salary(y/n) ?")
            if(ans.lower() == 'y'):
                empSal = input("Enter Emp Salary: ")
                allEmp[empId].salary  = empSal
            print("Updated Details: \n")
            allEmp[empId].getData()
        else:
            print(empId, "is not present..")
    