# Walrus Operator --> It is a new addition to python 3.8 and allow you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but donot want to repeat the calculation 

# Walrus operator is represented by the := syntax and can be used in a variety of contexts including while loop and if statements.

#or

# walrus operator assigns values to variables as part of a larger expression.

a=True 
print(a:=False)
print(a)

numbers=[1,2,3,4,5,6]
while(n:=len(numbers))>0:
    print(numbers.pop())
    
    

happy=True
print(happy)

print(happy:=True)

#without walrus
foods=list()
while True:
    food=input("What food do u like?:")
    if food == "quit":
        break
    foods.append(food)


    
#with walrus
foods=list()
while (food:=input("What food do u like?:")) != "quit":
    foods.append(food)
    
    