from array import *

arr=array("i",[1,3,4,6,7,8,9])

ele=99
pos=3
arr.append(0)

for i in range(len(arr)-1,pos,-1):
    arr[i]=arr[i-1]

arr[pos]=ele 

print(arr)

#deletetion of an element

arr=array("i",[1,4,6,7,8,9])

pos=4

for i in range(pos,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop()    
print(arr)    


#target sum

arr=array("i",[8,3,4,6,7,9])
arr=sorted(arr)
print(arr)
target_sum=11
low=0

high=len(arr)-1
while low<=high:
    current_sum = arr[low]+arr[high]
    if current_sum == target_sum:
        print(f"target sum  found at ele  {arr[low]} and {arr[high]}  index {low} and {high}")
        break
    elif current_sum < target_sum:
        low+=1
    else:
        high-=1


#dutch national flag

arr=array("i",[0,1,0,0,1,1,1,0,1,1,2,2,1,1,2,1,0,1,2])
low=0
mid=0
high=len(arr)-1

while mid < high:
    if arr[mid]==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid] 
        high-=1
print(arr) 




#Water Container

arr=array("i",[1,3,8,7,10,5])
ans=0
low=0
high=len(arr)-1
while low <= high:
    width=high-low
    lowest_height=min(arr[low],arr[high])
    volume=width*lowest_height
    ans=max(volume,ans)
    if arr[low] < arr[high]:
        low+=1
    else:
        high-=1  
print(ans)    





