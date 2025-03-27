#Seek() and tell() and other function
#seek and tell batatta hai ki file object and file position within a file.Build in module hota hai jo ki continuous interface provide karta hai reading and writing mai for various file object like files,pipes and in-memory buffers.

# with open("myfile.txt","r") as f:
#     print(type(f))
#     # Move to the 10th Byte in the File
#     f.seek(10)
    
#     #Read the next 5 bytes
#     data=f.read(5)
#     print(data)




#tell()
with open("myfile.txt","r") as f:
    print(type(f))
    # Move to the 10th Byte in the File
    f.seek(10)
    
    #Read the next 5 bytes
    print(f.tell())  # ye batata hai kaha tak humne seek kara hai
    data=f.read(5)
    print(data)
    
#truncate()
with open("sample.txt","w") as f:
    f.write("hello World3!")
    f.truncate(5)
    
with open("sample.txt","r") as f:
    print(f.read())

