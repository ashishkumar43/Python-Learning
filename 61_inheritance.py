#inheritance is simple 
 ## class make and with the help of we are using.
 #Problem is simple that is to we do for multiple claases and object we need to change in every code. 
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showdetails(self):
        print(f"the name of employee {self.id} is {self.name}")
    
class Programmer(Employee):
        def showlanguage(self):
            print("The default langugae is python")
        
                
# with the help of the object we can use the object.
e=Employee("Ashish kumar",412)
e.showdetails()
e1=Employee("Ashish kumar",412)
e1.showdetails()
e2=Employee("Ashish kumar",412)
e2.showdetails()
e2=Programmer("ashish",123)
e2.showlanguage()
       
        