#Super keywords --> it is used to refer the parents class.

class ParentClass:
    def parent_method(self):
        print("this is the parents methods..")
        
        
class ChildClass(ParentClass):  # Mai chahta hu ki parents class ka parents method call karu 
    def parent_method(self):
        print("this is the Child methods..")
        super().parent_method()
    def child_method(self):
        print("This is the child class method...")
        super().parent_method()  #Mai parents class ka parents method call karu with the help of super keywords karenge 
        
child_object=ChildClass()
child_object.child_method()
child_object.parent_method()

# With the help of Constructor i want to call it 

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name=name
        # self.id=id
        self.lang=lang
   #self.name=name   and self.id=id  to repeat it we use the super keywords that will call the constrcuore like super().__init__(name,id)
        super().__init__(name,id) 
            
ashish=Employee("ashish kumar","4220")
rohan=Programmer("rohan kumar","4324","python")
print("Ashish")


        
        

