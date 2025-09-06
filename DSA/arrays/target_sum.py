from array import *


arr=array("i",[1,5,8,34,45])

ar=sorted(arr)

target_sum=6
low=0
high=len(arr)-1
cureent_sum=0
while low < high:
    cureent_sum=arr[low]+arr[high]

    if cureent_sum ==target_sum:
        print(f"found  tagrget sum {target_sum} at {arr[low]},{arr[high]}")
        break
    elif target_sum > cureent_sum:
        low+=1
    else:
        high-=1
else:
    print(" not found an element ")            



