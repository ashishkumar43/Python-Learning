# Instance vs Class Variables.
#Instanse variables mai kya hai first instance variables ko dudhega agar wo mil jata hai to exectue kardega jo instance variables mai rahega.

# class variables wo hota hai to jo 

class Employee:
    companyname="Apple"  #class variable
    noofemployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02  #instance variables
        Employee.noofemployee+=1
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyname} is {self.raise_amount}")
    
emp1=Employee("As+hish")
#both will give the same result
emp1.showdetails()
        #or
Employee.showdetails(emp1) #if we remove the self keyword from showdetails then this line code take one postitional arguments.


emp1=Employee("Ashish")
emp1.raise_amount=0.03
emp1.companyname="Aple india"   #instanse variables
emp1.showdetails()
Employee.companyname="Google"   #instanse varibales
Employee.showdetails(emp1)

        