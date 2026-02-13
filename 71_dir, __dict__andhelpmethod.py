# dir, __dict__ and help method

#Dir method  (all the method are there in itself we can implement it)
#For list... 
x=[1,2,3]
print(dir(x))
print(x.__add__)

#For tuple
x=(1,2,3)
print(dir(x))
print(x.__add__)    # this is dunder method __annotations__


# __dict__  (It will give as a dictionary format...)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
        
p=Person("ashish",20)
print(p.__dict__)


# help() method (This is the function help to get documentation for an object including description of its attributes and methods)

print(help(Person))
