# String is an immutable 
a="ashish !!!!sonu kumar"
print(a)
print(a.upper())
print(a.lower())
a1="ashish!!!!!!!!!!!"
print(a1)
print(a.rstrip("!"))   #remove all the trailing character
print(a.replace("sonu","ashish"))
print(a.split(" "))   #list ban jati hai 
#captilalize
mysite="aShish is a GGood boy"
print(mysite.capitalize())
#Center 
str1="Welcome the ashish pythom code"
print(len(str1))
print(str1.center(50))
#Count
print(a.count("ashish"))to 
#endswith
print(str1.endswith("!!!"))
print(str1.endswith("code"))
print(str1.endswith("to",4,10))
#find
print(str1.find("the"))
print(str1.find("ok"))
#Index
print(str1.index("ashish"))
#isalpha numeric
str="Ashishisagoodboysir"
str1="welcome001"
print(str)
print(str.isalnum())
print(str1.isalnum())
ashish="AAshishisaGGOOD"
print(ashish.islower())
str1="wewanttodogood"
print(str1.isprintable())  #using spacebar
print(str1.istitle())
print(str1.swapcase())  # upper ko lowercase mai convert karenge
