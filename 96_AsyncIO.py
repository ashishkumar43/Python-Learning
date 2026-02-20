# AsyncIO in Python
# AsyncIO is a library to write concurrent code using the async/await syntax. It is used to write asynchronous code in Python. It is a single-threaded, single-process design that uses cooperative multitasking to achieve concurrency. It is used to write code that can run concurrently without blocking the main thread. It is used to write code that can run concurrently without blocking the main thread.

#or

# AsyncIo ek concurrent programming library hai jo async/await syntax ka use karke likha jata hai. Ye Python me asynchronous code likhne ke liye use hota hai.

import time

def function1():
    time.sleep(2)
    print("Function 1")
    
def function2():
    time.sleep(2)
    print("Function 2")
    
def function3():
    time.sleep(2)
    print("Function 3")

function1()
function2()
function3()
 # This will print the output one by one after 2 seconds. This is a blocking code. 
 

# Use Case for AsyncIO:
# 1. Web Scraping: manloo hum koi image net se download karna chahte hai to ek download ho rhi hai uske turant dursri download kar sakte hai. but in python ye possible nahi hai but with the help of AsyncIO we can do this.

async def function1():
    time.sleep(2)
    print("Function 1")
    
async def function2():
    time.sleep(2)
    print("Function 2")
    
async def function3():
    time.sleep(2)
    print("Function 3")
async def main():
    await function1()  # await is used to wait for the function to complete before moving to the next line of code. It is used to wait for the function to complete before moving to the next line of code.
    await function2()
    await function3()

# I want to run all the functions concurrently without waiting for each other. So, I will use asyncio to run all the functions concurrently.

import asyncio

async def function1():
    await asyncio.sleep(2)
    print("Function 1")
    return "Function 1 Completed"
    
async def function2():
    await asyncio.sleep(2)
    print("Function 2")
    
async def function3():
    await asyncio.sleep(6)
    print("Function 3")
async def main():
    task=asyncio.create_task(function1())  # create_task is used to create a task for the function. It is used to create a task for the function. or ye karne se kya hoga jab usko time lagega to wo usko wait nahi karega balki turant dursri function ko run kar dega. isse acha organization nhi milta hai code ka. isliye hum use karte hai gather function ka.
    await function1() 
    await function2()
    await function3()
    
    #Gather function use 
async def main():
    l=asyncio.gather(
        function1(), 
        function2(), 
        function3())
    print(l)  # gather function is used to run all the functions concurrently and it returns a list of results. It is used to run all the functions concurrently and it returns a list of results.
    
    
# Requests module we will use
import asyncio
import requests

async def function1():
    url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWJWDXcxT_d2_sUjKuLHsLgV0k7x_S8euHfg&s'
    response=requests.get(url)
    open('response.txt','wb').write(response.content)
    print("Function 1")
    return "Function 1 Completed"
    
async def function2():
    url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEbDbol6pGj1wGcKfoaCzVyzzCiNuXVpHGRg&s'
    response=requests.get(url)
    open('response.txt','wb').write(response.content)
    print("Function 2")
    
async def function3():
    url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWJWDXcxT_d2_sUjKuLHsLgV0k7x_S8euHfg&s'
    response=requests.get(url)
    open('response.txt','wb').write(response.content)
    print("Function 3")
async def main():
    task=asyncio.create_task(function1())  # create_task is used to create a task for the function. It is used to create a task for the function. or ye karne se kya hoga jab usko time lagega to wo usko wait nahi karega balki turant dursri function ko run kar dega. isse acha organization nhi milta hai code ka. isliye hum use karte hai gather function ka.
    await function1() 
    await function2()
    await function3()
    
    #Gather function use 
async def main():
    l=asyncio.gather(
        function1(), 
        function2(), 
        function3())
    print(l)  # gather function is used to run all the functions concurrently and it returns a list of results. It is used to run all the functions concurrently and it returns a list of results.