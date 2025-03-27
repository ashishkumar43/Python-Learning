#Lambda function (it is a small anonymous function without a name)
# Lambda arguments: expression
# def double(x):
    # return x*2
# print(double(5))

def appl(fx,value):
    return 6+fx(value)
# OR
double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y: (x+y)/2

print(double(5))
print(cube(5))
print(avg(5,3))
print(appl(cube,2))
print(appl(lambda x:x*x*x,2))