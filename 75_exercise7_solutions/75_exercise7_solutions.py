import os

# files=os.listdir("75_exercise7_solutions/clutterfolder")
# for file in files:
#     print(file)

# files=os.listdir("75_exercise7_solutions/clutterfolder")
# for file in files:
#     if file.endswith(".png"):
#         print(file)
    
files=os.listdir("75_exercise7_solutions/clutterfolder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"75_exercise7_solutions/clutterfolder/{file}",f"75_exercise7_solutions/clutterfolder/{i}.png")
        i=i+1
    
    
# os.rename("75_exercise7_solutions/clutterfolder/file.txt", "75_exercise7_solutions/clutterfolder/ashish.txt")
# print("ashish kumar")