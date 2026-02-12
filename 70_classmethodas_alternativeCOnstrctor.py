# Class Methods as Alternative Constructors

#This is normal method 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employee("Ashish",12000)
print(e1.name)
print(e1.salary)

string="Ashish-12000"
e2=Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)

#Example 
'''
a=ashish-12-python
a.split("-")
output --> [ashish,12,python] aa jayega...
'''

#With  Class Methods as Alternative Constructors use it

#jitna bhi clutter hai wo hum class ke under bhej de taki jo humara main fucntion rehta hai wo easy rahe.. only class ko use karo aur class humara package mai se aata hai ...
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],string.split("-")[1]) #Particular data ka format pass karo..
        
e3=Employee.fromStr(string)
print(e3.name)
print(e3.salary)
