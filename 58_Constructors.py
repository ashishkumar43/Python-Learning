# #Constructor (ek object banane mai madad karta hai)
# class Person:
#     name="ashish"
#     occ="data scientist"
    
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
        
# a=Person()
# # print(a.name)
# # print(a.occ)
# a.name="sonu"
# a.occ="manager"
# a.info()




class Person:
    #constructor none return karta hai.
    # def __init__(self):  # default constructor hai dunder method also constructor koi arguments nhi leta only take self.
    def __init__(self,o,n):  #paramter constructor pass for constructor call take parameter a,b and self automatically
        print("HELLO I AM ASHISH ") 
        self.name=n
        self.occ=o
        
        
    # name="ashish"
    # occ="data scientist"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=Person("ashish","good_developer")
b=Person("sonu","HR")
# c=Person()
# c=Person(1,2,3)  # error dega kyoki self aapne aap leta hai 2 parametet pass karna hoga
a.info()
b.info()

# print(a.name)
# print(a.occ)
# a.name="sonu"
# a.occ="manager"
# a.info()