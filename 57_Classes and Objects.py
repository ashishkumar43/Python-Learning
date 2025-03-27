#Class and Object
# class Person:
#     name="ashish"
#     occupation="Data Scientist"
#     networth=10
#     age=21
# a=Person()
# # a.name="kumarSonu"
# # a.occupation="DataAnalayst"
# print(a.name,a.occupation)


class Person:
    name="ashish"
    occupation="Data Scientist"
    networth=10
    age=21
    #self paramater is a wo object jsike liye ye function call kiya ja rha hai
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()  #object is a instance of the class used to access the properties of the class.
b=Person()  #object is a instance of the class used to access the properties of the class.
# eg object = class name()
a.name="kumarSonu"
a.occupation="DataAnalayst"

b.name="Greatashish"
b.occupation="Engineer"
# print(a.name,a.occupation)
a.info()  #ye method jiske liye a object self mai jayega
b.info()