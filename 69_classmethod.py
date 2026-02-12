# Class Method --> a class method is a  type of method that is bound to class and not instance of the class.

class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        
    @classmethod   # a decorator
    def changeCompany(cls, newCompany):
        cls.company= newCompany  # this is instancse only not class and here cls treat as a instanse not class if we want a class come then we use the @classmethod so that cls take as a class milega not instance
        
e1=Employee()
e1.name="ashish"
e1.show()
e1.changeCompany("Telsa")
e1.show()
print(Employee.company)