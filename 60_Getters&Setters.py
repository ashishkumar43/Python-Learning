class Myclass:
    def __init__(self,value):
        self._value=value
        
    def show(self):
        print(f"Value is {self._value}")
        
    @property  # property decorator bhi hai ye or this is a getter to get the value 
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter  # ten_value.setter decorator bhi hai ye or this is a setter to take the value 
    def ten_value(self,new_value):
        self._value=new_value/10
    
obj1=Myclass(10)
obj1.ten_value=69  # this can not be done. or this is wrong way to set the value
print(obj1.ten_value)  #getter ban jayega
obj1.show()