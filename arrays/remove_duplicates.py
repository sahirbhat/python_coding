from array import *

arr=array("i",[1,1,1,22,22,44,55,55,55,90,90])
arr_without=array("i")

for i in arr:
    if not arr_without or arr_without[-1]!=i:
        arr_without.append(i)
print(arr_without)        