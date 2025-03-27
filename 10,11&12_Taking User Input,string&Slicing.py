# input function
a=input("enter your name:\n")
print(a)
x=input("enter the no is")
y=input("enter the no is")
print(float(x)+float(y))

# #String
name="ashish"
another='ok'
print(name+"another")
print("hllo:"+another)
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# String slicing
fruit="khela"
print(len(fruit))
print(fruit)
print(fruit[0:4])   # including 0 and but not 4
print(fruit[1:4])   # including 1 and but not 4
print(fruit[:4])   # including  and but not 4
print(fruit[0:-3])   # including 0 and but not 4
print(fruit[0:len(fruit)-3])   # including 0 and but not 4
print(fruit[-1:len(fruit)-3])   # including 5-1=4 and but not 5-3=2s=
print(fruit[:])   # including  and but not 
print(fruit[-3:-1])   # ye interpret karega 5-3=2 and 5-1=4

# small quiz
# name="ashish"
# print(name[-4:-2])
name="ashish"
print(len(name))
print(name[0:5])
print(name[len(name)-4:len(name)-2])
