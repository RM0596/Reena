class Employee:
    def __init__(self,role,depart,salary):
        self.role = role
        self.depart = depart
        self.salary = salary
    
    def showdetails(self):
        print(self.role ,"Role" , self.depart , "depart", self.salary , "salary")

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","25000")

Emp1=Employee("Account","Finance","15000")
Emp1.showdetails()

Eng1 = Engineer("Rina",32)
Eng1.showdetails()
