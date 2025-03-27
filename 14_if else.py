# # if-else
# a=int(input("Enter your age: "))
# print("Your age is ",a)
# #conditional statement
# #<,>,>=,<=,==,!=
# # print(a>18)
# # print(a<=18)
# # print(a==18)
# # print(a!=18)
# if(a>18):
#     print("You Can Drive")
# else:
#     print("You Cannot Drive")

# appleprice=210
# budget=200
# if(appleprice<=budget):
#     print("Alexa,add 1kg of apples to the cart")
# else:
#     print("Alexa,do not add apples to the cart")
    
#el-if
# num=int(input("Enter the number : "))
# if(num>0):
#     print("Number is Positive")
# elif(num==0):
#     print("Number is zero")
# else:
#     print("Number is negative")
# print("Now I am Happy ")

#Nested if-else
num=int(input("Enter the number is :"))
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
print("I am Happy")