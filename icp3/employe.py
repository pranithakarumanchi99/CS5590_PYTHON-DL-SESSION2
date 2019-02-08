class Employee():
    empCount = 0
    SumSalary =0
    Avg =0

    def __init__(self, eid, name, salary, Jid):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = Jid
        Employee.empCount += 1
        Employee.SumSalary += self.salary

    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", Jid: ", self.did)
class FullTimeEmp(Employee):
    def __init__(self, eid, name, salary, Jid, exp):
        Employee.__init__(self, eid, name, salary, Jid)
        self.exp = exp
    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did, ",Experience:", self.exp)



emp1 = Employee(1, "Pranitha", 50000, 10)
emp2 = Employee(2, "Sushma", 35000, 20)
emp3=FullTimeEmp(3, "Chandini", 40000, 20, 6)
# Total employee and average salary
print("Total Employees %d" % Employee.empCount)
print("Average salary of the employees is", (Employee.SumSalary/Employee.empCount))
print(emp1.displayEmployee())
print(emp2.displayEmployee())
print(emp3.displayEmployee())