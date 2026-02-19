# News API.org that is the api (search news with code)

# Exercise 10
'''Use the NewsAPI and the requests module to fetch the daily news realted to different topics.
Go to: https://newsapi.org/ and expore the various options to build your applications.'''

import requests

url="api key enter here"
r=requests.get(url)
print(r.text)



# As string aagyi 
import requests
query=input("what type of news are u interested in ?")
url=f"https//newsapi.org/v2/everything?q={query}&from=2024-1-3030"
r=requests.get(url)
print(r.text)


# As json parse karna hai.
import requests
import json

query=input("what type of news are u interested in ?")
url=f"https//newsapi.org/v2/everything?q={query}&from=2024-1-3030"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:  # to access the dictionary use it --> news["articles"]
    print(article["title"])
    print(article["description"])