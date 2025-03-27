# read() and readlines() and other methods
# readline tell about read the file line by line
# f=open("myfile.txt","r")
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
#     print(line)



# f=open("myfile.txt","r")
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
#     m1=int(line.split(",")[0])
#     m2=int(line.split(",")[1])  # we use int because thsi give the output in string format
#     m3=int(line.split(",")[2])
#     print(f"Marks of student {i} in maths is:{m1*2}")
#     print(f"Marks of student {i} in english is:{m2*2}")
#     print(f"Marks of student {i} in SST is:{m3*2}")
#     print(line)


#writelines
f=open("myfile2.txt","w")
lines=["line1\n","line2\n","line3\n","line4\n"] #line jo bhi add karna ho karna padega
f.writelines(lines)
f.close()