class Employee:
    def __init__(self,name,age,phone,adress,salary):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=adress
        self.salary=salary
    def printSalary(self):
       print("Salary=",self.salary);

class Officer(Employee):
   def __init__(self,name,age,phone,adress,salary,specialization):
     self.spec=specialization
     super().__init__(name,age,phone,adress,salary)
    #Employee.__init__(self,name,age,phone,adress,salary)
   def  getofficier(self):
      print(self.name, self.age, self.phone, self.address, self.salary, self.spec)

class Manager(Employee):
    def __init__(self,name,age,phone,adress,salary, department):
        self.dept=department;
        super().__init__(name, age, phone, adress, salary)

    def getmanager(self):
        print(self.name, self.age, self.phone, self.address, self.salary, self.dept)


o=Officer("Susan",32,9887677667,"kakkanad",20000,"Networking",)
o.printSalary()
o.getofficier()
M=Manager("Anoop",22,988967467,"EKM",40000,"ME")
M.printSalary()
M.getmanager()