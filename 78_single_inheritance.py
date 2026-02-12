#Single Inheritance --> single inheritance is type of inheritance where a class inherits the properties and behaviour from a single parents class.

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def make_sound(self):
        print("Sounds made by the animal ")
        
class Dog(Animal) :
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")  
        self.breed=breed
        
        def make_sound(self):
            print("Bark")
            
d=Dog("Dog","Doggerman")     
d.make_sound()

a=Animal("Dog","Dog")
a.make_sound()
    
    
#Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat.