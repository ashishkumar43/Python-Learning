# Regular Expression or regex -->it is a powerful tool for working with strings and text data. 
# Simple pattern matching ko hum simple check karenge ki string me koi particular word hai ya nahi.
# Regular expression me hum pattern define karte hai jise hum string me search karna chahte hai.

# a package is import name as re that is built in package in python for regular expression.

import re
pattern = "abc"
text = "abc is a simple pattern matching example."

match = re.search(pattern, text)
print(match)  

#Metacharacters in regular expression--> it is used for defining the pattern in regular expression.

import re
pattern = r"[A-Z]+imple" # r is a raw string that is used to parse the string
text = "abc is a Simple Pattern matching example."

match = re.search(pattern, text)  # re search to hota hai na wo pehle match ke baad stop ho jata hai.
print(match)  

matches=re.finditer(pattern,text)
for match in matches:
    print(match.span())  # span() method is used to get the start and end index of the match in the string.
    print(type(match.span()))  # it is a tuple that contains the start and end index of the match in the string.
    
# Two important websites for regular expression:
# regexr.com
# pythonorg.com