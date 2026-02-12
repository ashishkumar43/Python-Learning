# Mutiple inheritance --> Multiple parents class and only one child class.

class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")
    
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")
    
class DancerEmployee(Dancer, Employee):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
        
o=DancerEmployee("Ashish","Kathak")
print(o.name)        
print(o.dance)
o.show()        

#Special method is MRO (Method resoltion order)
print(DancerEmployee.mro())
