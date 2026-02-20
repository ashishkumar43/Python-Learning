#Multi Processing --> multiple process spawn karega(child process spawn karega and spawn means hota hai process ko start karna...) or in english multiple process provides a single way to run the nultiple processes in parallel.


import multiprocessing
import requests

def downloadfile(url,name):
    print(f"Started Downloading {name}")
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")

url="https://picsum.photo/200"
process=[]
for i in range(50):
    # downloadfile(url,i)
    p=multiprocessing.Process(target=downloadfile,args=[url,i])
    p.start()
    process.append(p)
        
for p in process:
    p.join()