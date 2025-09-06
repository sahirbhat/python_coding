from array import *

arr=array("i",[45,67,8,1,3,8,3,-9,76])

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr) 
           