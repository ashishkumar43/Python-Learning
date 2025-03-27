# #Exception Handling
# a=int(input("enter the number is"))
# print(f"Multiplication table of {a} is :")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}x{i}={int(a)*i}")
# # except Exception as e:
#     # or
# except:
#     print("sorry some errror occured")
    
# print("some imp lines of code")
# print("End of program")

# try:
#     num=int(input("Enter the integer:"))
#     a=[6,4]
#     print(a[num])
# except ValueError:
#     print("Number enterd is not string")
# except IndexError:
#     print("Index error")
    

#finally (Execute hota hai humesa chahe error aaye ya na aaye )
try:
    l=[1,4,5,7]
    i=int(input("enter the index:"))
    print(l[i])
except:
    print("Some error occured")
# finally:
#     print("I am always executed")
print("I am always executed")

#finally mai same chij function mai dallenege tab pata chalega
#finaaly ka matlab hai chahiye tum try mai return ho jao par mai to finally tak jaunga 

def funct1():
    try:
        l=[1,4,5,7]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")
# print("I am always executed")

x=funct1()
print(x)