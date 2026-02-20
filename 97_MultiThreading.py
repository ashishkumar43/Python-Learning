# Multi threading in python
# why we use it --> i want to download the file of 10 gb and i will have do to download one by one this will waste our time and resources and for easy we can simple do is we can download it with the use of multi threading.

import threading
import time 

# Indicates some task being done

def func(seconds):
    print(f"sleeping for {seconds}seconds")
    time.sleep(seconds)
    
time1=time.perf_counter()   # perf_counter() is the performance counter that count the performance.    
#Normal Code 
# func(3)
# func(2)
# func(1)
# time2=time.perf_counter()   
# print(time2-time1) 

# Jaise take an example koi person have gone to the restaurant and tell that mujhe panner butter masala, lassi and nan khana hai aur jo banene wala hoga wo ek ek karke banayega to bahut time lagega so we can say that 2 se 3 aadmi agar banaye to jaldi ban jayaga wohi multi threading concept hai...

# Same code using threads
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()
time2=time.perf_counter()   
print(time2-time1) 


#Concurrent.future
from concurrent.futures import ThreadPoolExecutor
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l=[3,2,1,4]
        results=executor.map(func,l)
        for result in results:
            print(result)

