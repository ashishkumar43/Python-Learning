#file io
# #Reading the file
# f=open("myfile.txt","r") # r is the mode to read kar sakte hai "r" and write through kar sakte hai "w" nd append kar sakte hai "a"
# f=open("myfile.txt","rt") # rt is open as txt 
# f=open("myfile.txt","rb") # rb is open as png,images,file,pdf wagerah 
# f=open("myfile2.txt","w") # r is the mode to read kar sakte hai "r" and write through kar sakte hai "w" nd append kar sakte hai "a"
# f=open("myfile.txt") 
# # print(f)

# text=f.read()
# print(text)
# f.close()

# Writing the file
# f=open("myfile2.txt","w") # r is the mode to read kar sakte hai "r" and write through kar sakte hai "w" nd append kar sakte hai "a"
# f.write("hello ashish you have write the content")
# f.close() 

# # Append the file
# f=open("myfile2.txt","a") # append mode mai open karega isme helloashish ke piche add hota jayega
# f.write("hello ashish you have write the content")
# f.close() 
# OR
#with statement tells about the automatically close the file with it
with open("myfile2.txt","a") as f:
    f.write("hello ashish i am inside")