from array import *

arr=array('i',[88,44,5,6,33,55,67,77,34,55,66,45])
# dup=[]
# for i in arr:
#     n=arr.count(i)
#     if n>1 and  i not in dup:
#         dup.append(i)
# print(f"the element duplicate is {dup}.number of times is {n}")

arr=array('i',[88,44,5,6,33,55,67,77,34,55,66,45])
dup=[]
for i in arr:
    if arr.count(i) > 1 and  i not in dup:
        dup.append(i)
print(dup) 

# topics to learn
#   try catch
#    logging
#    decorator
#    itraror generator and enumerater
#    Files
#    requets
#    json loads and dumps
#    threading

#    class object 
#    ineheritence
#    polymoprhis 
#    override 
#    etc
#     patterns 
# deep copy shallow copy





   


