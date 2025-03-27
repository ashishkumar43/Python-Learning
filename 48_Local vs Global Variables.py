# #Global and local variable
# x=4
# print(x)


# def hello():
#     x=5
#     print(f"The local x is {x}")
#     print("Hello Ashish_Kumar")
    
# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")

x=10 #Global variable

def my_function():
    global x
    x=4
    y=5 #Local variable
    print(y)
    
    
my_function()
print(x)
# print(y)# thsi will cause an error beacuse y is a local variable and is not accessible outside the function
    
    