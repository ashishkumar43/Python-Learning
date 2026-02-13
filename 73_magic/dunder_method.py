# Dunder Method --> this is a special method that can defined in your class and when invoked it will give a powerful way to manipulate the behaviour and magic method is a dunder method , symbol is __(double underscore)

class Employee:
    name="Ashish"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1 
        return i

e=Employee()
print(e.name)
print(len(e))  #this wont work beacuse direcly len method is not work in the class and object


# With __init__()
class Employee:
    def __init__(self,name):
        self.name=name
        
        
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1 
        return i
    
    # and use it for __str__()    
    def __str__(self):
        return f"the name of the Employee is {self.name} str"

    # and use it for __repr__() --> call back kar jata hai repr pe jab str nhi milta hai to... or the simple meaning of the repr method is to recreate the object.
    def __repr__(self):
        return f"the name of the Employee is {self.name} repr"
    
    
    # __call__()
    def __call__(self):
        print("hey i am ashish")
     
    
e=Employee("Ashish")
print(e.name)
            
# Now we will do with the help of import 
# and use it for __str__()
        