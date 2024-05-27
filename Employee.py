class Employee:
    def __init__(self,Name,Job_title,Salary):
        self.Name=Name
        self.Job_title=Job_title
        self.Salary=Salary

    def display(self):
        print(f"The Employee {self.Name} job title {self.Job_title} the Salary {self.Salary} ")

    def calculate(self):
        return self.Salary * 12

    def give_raise(self, percentage):
        self.Salary = self.Salary * (1 + (percentage / 100))


Emp1=Employee("YashVerma","frontEndDeveloper",45000)
# Emp.display()

Emp1.calculate()
Emp1.give_raise(10)
Emp1.display()