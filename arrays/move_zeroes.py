from array import *

arr=array("i",[0,3,5,6,8,0,7,0,4,6,0])
low =0
high=len(arr)-1

while low < high:
    if arr[low]==0 and arr[high]!=0:
        arr[low],arr[high]=arr[high],arr[low]  
        # print(arr[low],arr[high])

    low+=1
    high-=1
print(arr) 


from array import array

arr = array("i", [0, 3, 5, 6, 8, 0, 7, 0, 4, 6, 0])
result = array("i")

# Append all non-zero elements
for num in arr:
    if num != 0:
        result.append(num)

# Append all zeros
for num in arr:
    if num == 0:
        result.append(num)

print(result)




