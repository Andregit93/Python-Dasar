class Employee:
    empCount = 0
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
        
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
        
    def Demployee(self):
            print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", "2000")
emp2 = Employee("Manni", "5000")

emp1.Demployee()
emp2.Demployee()

print ("Total Employee %d" % Employee.empCount)