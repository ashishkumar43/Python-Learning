# Generators --> generators ka use hota hai on the fly value generate karne ke liye, ye memory efficient hote hain, ye ek baar me ek value generate karte hain, jab tak ki unhe next value ke liye call na kiya jaye. or generators ko hum iterators bhi kehte hain, ye iterables hote hain, lekin ye list ya tuple ki tarah pura data memory me store nahi karte, balki jab unhe call kiya jata hai tabhi value generate karte hain.

# Generators value ko store nhi karte, or generators object ko store karke rakhta hai uske bannane ki samagrai store karke rakhta hai

#Creating a generator
# i can create generator using yield statement in function and return the yield value and suspended the execution of the function until the next value is requested 
def my_generator():
    for i in range(500):
        yield i
        
gen=my_generator()
# print(next(gen))
# print(next(gen))

# or 

for j in gen:
    print(j)


'''#Generator(ye generator value talta hai lazy hai) advantage:
1. on the fly value generate 
2. fast execution   
3. memory efficient (memory store karke nhi rakhta hai)'''
    