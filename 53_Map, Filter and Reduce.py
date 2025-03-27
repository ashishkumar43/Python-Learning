# #Map,filter and reduce 
# #Map
# def cube(x):
#     return x*x*x
# print(cube(2))
# l=[1,2,3,5,3,1,4]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))
# # shortcut
# newl=map(cube,l)
# newl=list(map(cube,l))
# newl=list(map(lambda x:x*x*x,l))

# print(newl)


# #filter 
# def filter_function(a):
#     return a>4
# newnewl=list(filter(filter_function,l))
# print(newnewl)

# Reduce
from functools import reduce
#list of numbers
numbers=[1,2,3,4,5]
numbers=[3,3,4,5]
numbers=[6,4,5]
numbers=[10,5]
numbers=[15]
#calculate the sum fo the numbers using the reduce function
def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)

#print the sum
print(sum)
    
