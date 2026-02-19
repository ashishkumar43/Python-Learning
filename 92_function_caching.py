# Function Caching  -->> ek program 10 sec mai chal rha hai bahut computational costly hai so hum iske liye fucntion caching ka use karenge so that caching to store karke rakhe.
# the module which are used in this is functools.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(4)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(7))
print("done for 7")

# iske niche ye cache ko sidha store kar lega jisse hum memoization kehte hai.
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(7))
print("done for 7")

# aur jab ek program program ko rerun karenge to wo caching clear ho jayegi and phirsse compute karega value
