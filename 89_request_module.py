# Request module in python 
# In python request module is a http library that enables developers to send http request in python. This module enables u to send the http request using python code and make it possible to interact with the APIs and web services..

#pip install requests

import requests
response=requests.get("https:/www.google.com")
print(response.text)

#posts requests
url="https:/www.google.com/posts"

data={
    "title":"coding",
    "name":"ashish",
    "userid":1
}

headers={
    "content-type":"application/json; charset=UTF-8"
}

response=requests.post(url,headers=headers,json=data)


# bs4 --> beautiful soup 
import requests
from bs4 import BeautifulSoup
url="https:/www.google.com/posts"
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())

for heading in soup.findall("h2"):
    print(heading.text)
    