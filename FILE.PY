import os
import re
# files=os.listdir()

# for f in files:
#     if os.path.isfile(f):
#         with open(f, "r") as fi:
            
#                 l=fi.read()
#                 print(l)
#challenge 2:
if  os.path.exists("dictionniar1.py"):
      with open("dictionniar1.py", "r") as fi:
                    l=fi.read()
                    print(l)

else:
       print("none")
#challenge3:
l=["a","b","c","d"]



# for  i in range (len(l)):
#         os.makedirs(f"/home/kawkaw/Documents/{l[i]}")
        
#challenge 6:
l=os.listdir()
l2=[]
f=lambda x:re.search(r"\.txt",x)
l2=list(filter(f,l))
print(l2)



               
     
