# #enumerate function
marks=[12,15,68,45,23,1,1,5]

# for mark in marks:
#     print(mark)
#     if(index==3):    #linter (error obvious hai to)
#         print("ashish","awesome!")

#index=0
# for mark in marks:
#     print(mark)
#     if(index==3):    #linter (error obvious hai to)
#         print("ashish","awesome!")
#         index=index+1

# use enumerate( ek hi line mai index aur uski value dedega aur string ke sath bho hota hai)
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("ashish","awesome!")
        
#unpack
# use v to unpack
for v in enumerate(marks):
    print(mark)
    if(index==3):
        print("ashish","awesome!")

# use enumerate( ek hi line mai index aur uski value dedega aur string ke sath bho hota hai)
fruits=["apple","banana","mango"]
for index,fruit in enumerate(fruits):
    print(index,fruit)