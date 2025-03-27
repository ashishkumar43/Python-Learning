#List (Store multiple item in one variable or  ek naam ke andar bahut sari value rakhna chahte hai)
#in list value can be added but in tuple we cannot
# l=[3,5,7]
# print(l)
# print(type(l))

# marks=[3,5,6]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(type(marks))
# print(marks[2])
# #print(marks[3])
marks=[3,5,6,"ashish","True"]
# print(len(marks))
# print(marks)

# if 8 in marks:
#     print("Yes")
# else:
#     print("No")
# #Same thing applies for strings as well
# if "as" in marks:
#     print("yes")
    
# marks=[3,5,6,"ashish","True",4,6,7,10]
# print(marks[1:4])
# print(marks[1:4:3])

#list comprehension  (kisi bhi list se ek new list banana hai usse kehte hai)
# lst=[i for i in range(4)]
lst=[i*i for i in range(5)]
# print(lst)
# lst=[i*i for i in range(10) if i%2==0]
print(lst)
