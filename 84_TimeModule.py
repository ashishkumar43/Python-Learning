#Time module --> it is build in function hai jo humme time related operation karne mai help karta hai.
'''
import time
def usingwhile():
    i=0
    while i<50000:
        i=i+1
        print(i)
        
def usingfor():
    for i in range(50000):
        print(i)

init=time.time()         # this will give the time in sec since 1917
usingfor()
t1=(time.time()-init)
init=time.time()         # this will give the time in sec since 1917
usingwhile()
print(time.time()-init)
print(t1)

'''
# Time Sleep

# import time
# print(4)
# time.sleep(2)  # time.sleep wait the time for 2 sec after that i will execute.
# print("this is printed after 2 seconds")

#Time.strftime() -->> it is a method gives a time value as a string based on the specific format.
import time
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(formatted_time)