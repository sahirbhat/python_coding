from array import *

arr=array("i",[6,4,8,9,2,3])

low=0
high=len(arr)-1
capacity=0
max_capacity=0

while low < high:
    width=high-low
    min_hieght=min(arr[low],arr[high])
    capacity=width*min_hieght
    max_capacity=max(max_capacity,capacity)

    if arr[low] < arr[high]:
        low+=1
    else:
        high-=1
print(max_capacity)  
          


