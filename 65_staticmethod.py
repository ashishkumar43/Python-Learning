# static method ka use tab kiya jata hai jab class ke instance ki need nhi rehti hai.

#static method mai without self hum use kar sakte hai chalega @staticmethod ek decorator hai and with class ka use bhi call kar sakte hai aur normal fucntion ki tarah use hota hai.

class Math:
    def __init__(self,num):
        self.num=num
        
    def addtonum(self,n):
        self.num=self.num+n
        
    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(1,2))


