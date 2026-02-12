#Multilevel inheritance in python --> grandfather --> father --> child 
# base class --> derived class1 --> derived class2

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def showdetails(self):
        print (f"Name: {self.name}")
        print (f"Species: {self.species}")
        
class Dog(Animal) :
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")  
        self.breed=breed
        
        def showdetails(self):
            Animal.showdetails(self)
            print(f"Breed: {self.breed}")
            
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color=color
        
    def showdetails(self):
        Dog.showdetails(self)
        print(f"Color:{self.color}")
        
        
            
o=GoldenRetriever("Tommy","black")
o.showdetails()

'''#IS order mai print karega 
print (f"Name: {self.name}")
print (f"Species: {self.species}")
print(f"Breed: {self.breed}")
print(f"Color:{self.color}")'''

o=Dog("tommy","Black")
print(GoldenRetriever.mro())