# design an employee management system where :
# there is 1 base class employee with attributes nname ,id, and salary.
#  A derived class manager has an additional attribute bonus and a method to calculate total salary (salary + bonus).   
# The program should allow the user to input employee and manager details and display their information along with the total salary for the manager.

class Employee:
     def __init__ (self,name,id,salary):
       self.name=name
       self.id=id
       self.salary=salary
     def display_employee(self):
         print("Employee details: ")
         print("\n")               
         print("Employee name:",self.name)
         print(" employee id:",self.id)
         print(" Employee salary:",self.salary)
     

class Manager (Employee):
    def __init__(self,name,id, salary,bonus):
        super().__init__(name,id,salary)
        self.bonus=bonus
    def total_salary(self):
        return self.salary + self.bonus    
    def display_Manager(self):
        self.display_employee ()
        print("----------------------------")
        print("Manager details: ")
        print("\n")
        print("Manager name:",self.name)
        print("Manager id:",self.id)
        print("Manager salary:",self.salary)
        print("Manager bonus:",self.bonus)
        print("Manager total salary:",self.total_salary())

name=input("Enter employee name: ")
id=int(input("Enter employee id: "))
salary=float(input("Enter employee salary: "))       

m_name=input("Enter manager name: ")
m_id=int(input("Enter manager id: "))
m_salary=float(input("Enter manager salary: "))
bonus=float(input("Enter manager bonus: "))

e=Employee(name,id, salary)
m=Manager(m_name,m_id,m_salary,bonus)

e.display_employee()
m.display_Manager()     