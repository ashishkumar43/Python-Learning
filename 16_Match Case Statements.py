 # work in pyhton 3.10
 #similar to switch case in cpp,c 
 # But in python switch case mai break nhi lagete hai jo condition true hogi hai wo chlegi
x=int(input("Enter the value of x "))
# x is a variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x,"not 90")
    case _ if x!=80:
        print(x,"not 80")

 