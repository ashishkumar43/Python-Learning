#if __name__=="__main__"  # file ko kahi aur se import karoge to lagana important hai 
# import aashish   #aashish.welcome ko comment kara to ek baar print hoga hey you are welcome from ashish
# aashish.welcome()   #print 2 times hey you are welcome from ashish


def welcome():
    print("hey you are welcome from ashish")

print(__name__)   # yahi se run ho rha hai program 
if __name__=="__main__":   # isko yahi se run kiya ja rha hai to welcome chalega warna nhi chalega 
    welcome()
