# WAP to greet you good morning,good afternoon,goodevening and also use time module to get the current hour.
# time=int(input("Enter the time:"))
# print("Time is ",time)
# if(time>=5 and time<12):
#     print("Good Morning Sir")
# elif(time>=12 and time<4):
#     print("Good AfterNoon Sir")
# else:
#     print("Good Evening Sir")

import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=time.strftime("%H")
print(timestamp)
timestamp=time.strftime("%M:")
print(timestamp)
timestamp=time.strftime("%S:")
print(timestamp)

