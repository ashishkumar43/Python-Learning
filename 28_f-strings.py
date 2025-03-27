#fstring (in string formatting in pyhton) 
# letter="Hello I am {} and i am {} good"
# letter="Hello I am {1} and i am {0} good"
name="ashish"
adj="good"
# print(letter.format(name,adj))

#use fstring
# print(f"Hello I am {name} and i am {adj} good")
# txt="for only {price:.2f} dollar"
# print(txt.format(price=50.34758))

price=50.34758
txt=f"for only {price:.2f} dollar"
print(txt)
# print(txt.format(price=50.34758))

print(f"{2*40}")
print(type(f"{2*40}"))

# If we print the whole string same use {{" "}}
print(f"Hello I am {{name}} and i am {{adj}} good")
