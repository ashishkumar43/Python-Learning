for i in range(12):
    if(i==10):
        break   # loop ko chorkar nikalja
    print("5 X",i+1,"=",5*((i+1)))

print("Loop ko chorkar Nikalja")



for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue  
    print("5 X",i+1,"=",5*((i+1)))

print("iteration ko chorkar Nikalja")