# set is a collection of well defined objects.
# why we use that is koi value repeat na ho jaise employeee gift le liya wo dubara na le paye 
# set are unordered very imp
#set mai 2 ek baar set mai chala gya phir iski value change nhi kar sakte 
set={2,3,6,3}
print(set)
info={"ashish",3,"good","ashish",7,3,7}
print(info)

#quiz (try to create an empty set.check using the type ()function whether the type of your variable is a set)
# ashish=set()        # this give the empty set
ashish={}            #this make the empty dictionary
print(type(ashish))  #this is a dictionary
 

for value in info:
    print("value of value is ",value)
    
    

#set method  
s1={1,4,5,6}
s2={1,3,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1,s2)
s1.update(s2)

# Symetric difference (dono mai common nhi hai)
# Atriangleb=AunionB-AintersectinB
cities={"delhi","up","bihar","rajakstha"}
cities2={"delhi","bihar","rajakstha","haryana"}
cities3=cities.difference(cities2)


#disjoint set (ek dusre se koi matlab nhi or no common element )
cities={"delhi","up","bihar","rajakstha"}
cities2={"delhi","bihar","rajakstha","haryana"}
cities3=cities.isdisjoint(cities2)
print(cities3)
# cities={"delhi","up","bihar","rajakstha"}
# cities.add("begusarai")
# print(cities)

# #remove/discard( remove error dega code nhi chalega aage but discard error nhi dega )
# cities={"delhi","up","bihar","rajakstha"}
# # cities.remove("begusarai")
# cities.discard("begusarai")
# print(cities)

# #pop
# cities={"delhi","up","bihar","rajakstha"}
# cities.pop()
# print(cities)
# # del cities

# #clear
# # cities.clear()

