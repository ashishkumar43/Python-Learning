# MEthod overriding -> it is the powerful feature that is used in oops to redefine a method in derived class.

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y

rec=shape(3,5)
print(rec.area())        

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius) # this will give the wrong output that is radius*radius  
        
    # def area(self):
    #     return 3.14* self.radius *self.radius
    
    #this is called the method overriding that override the area method of parents class.
    def area(self):
        return 3.14* super().area()  # this is calling the the parents class area method.
    
    
rec=shape(3,5)
print(rec.area())  

c=circle(5)
print(c.area())