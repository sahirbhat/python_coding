from array import *

arr=array("i",[1,4,5,6,7,9])
arr.append(0)
ele=99
pos=3
for i in range(len(arr)-1,-1):
    arr[i]=arr[i-1]

arr[pos] =ele

print(arr)


for i in range(pos,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop()    
print(arr)  


#tagrget sum

arr=array("i",[1,5,7,8])

target_sum=15
high=len(arr)-1
low=0
while low<=high:
    current_sum=arr[low]+arr[high]
    if current_sum==target_sum:
        print("found")
        break
    elif current_sum < target_sum:
        low+=1
    else:
        high-=1
else:
    print("not found")  



"""
    container max water

"""

arr=array("i",[1,4,9,5,7,3])

ans=0
low=0
high=len(arr)-1
while low <=high:
    width=high-low
    lht=min(arr[low],arr[high])
    max_cap=width*lht
    ans=max(max_cap,ans)
if arr[low] < arr[high]:
    low+=1
else:
    high-=1
print(ans)            

