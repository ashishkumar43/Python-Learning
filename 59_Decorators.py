#Decorators(ek function hai dusra fucntion hai update karke return kar deta hai)
# Syntax
# decorators_fucntion
# def my_function():
#     pass

# first greet karna hai phir my name is ashish print krna hai.
def greet(fx):
    # def mfx():
    def mfx(*args,**kwargs):             #*args takes as tuple and **kwargs takes as dictionary        print("Good Morning")
        fx(*args,**kwargs)
        # fx()
        print("Thanks for using this fucntion")
    return mfx

@greet
def hello():
    print("My name is ashish")
    
    # or 
    
greet(hello)()
def add(a,b):
    print(a+b)
    
# hello() 
# greet(add)(1,2)    #give the error  (add tak arguments pahuchega nhi) phir isme mfx fucntion mai *args 
# pehle decorate karo matlab greet karo print karna se pehle 


#logging module dhkena hai
