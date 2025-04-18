class Person:
    def __init__(self,fname,lname):
         self.firstname = fname
         self.lastname = lname
    def printnamae(self):
          print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
         super().__init__(fname,lname)
         self.graduationyear = year 

x = Student("Pragathi","student",2011)
x.printnamae()
print(x.graduationyear)

y = Student("Bindura","student",1986)
y.printnamae()
print(y.graduationyear)

