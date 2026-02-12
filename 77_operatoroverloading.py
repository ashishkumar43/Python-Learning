# Operator overloading in python --> ye ek tarika hai ki hum allows kar sakte hai developer ko uske mathematics operator ke behaviour ko change kar sakte hai.

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i+ {self.j}j+{self.k}k"  # this will return string and i want ki string na aaaye vector mai chahiye.
        
    def __add__(self,x):    #this is operator overloading. 
        return Vector(self.i+x.i, self.j+x.j,self.k+x.k)
    
v1=Vector(1,2,3)
print(v1)
v2=Vector(4,5,6)
print(v2)
print(v1+v2)
print(type(v1+v2))

# print(v1+v2)  # this line will give error because in vector we cant add two vector


        
        
        