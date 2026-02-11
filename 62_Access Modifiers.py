# In general  python access modifier is 
#public - >> we can access anywheere
#private ->> we can access only in class itself
#protected ->> we can access inside the classs and subclass(child class we can access).

# Access Specifier or accesss modifier
#Most imp things is in python there is no any access modifier or access specifer.

#Public access
class Employee:
    def __init__(self):
        self.name="ashish"       
a=Employee()
print(a.name)


#Private access
#in private __(double underscore) we can use it __ (it will work as a note we write meri gaddi maat le jao)

class Employee:
    def __init__(self):
        self.__name="ashish"       
a=Employee()
# print(a.__name)  #Cannot be accessed directly
print(a._Employee__name) #can be accessed indirectly
print(a.__dir__())  # we can access all method inside the __dir__()

#Name Mangling in python
# name mangling is a technique usd to protect the cllass-private and superclassprivate attributes from being overwrite by subclass.
#In mangling (a.__name) anyone can overwrite or used as a convetion aaisa bana dete hai koi used nhi kar paye to (a._Employee__name) aaisa ho jata hai.

#Protected
 
class student:
    def __init__(self):
        self.name="Ashish"
        
    def _funName(self):        #protected method
        return "Data scientist"

class subject(student):     #inherited class
    pass
        
obj=student()    
obj1=subject()        

#calling by object of student class
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())

 
