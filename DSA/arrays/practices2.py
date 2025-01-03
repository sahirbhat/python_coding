from array import *

#inserted element
arr=array("i",[34,45,66,99])
pos=3
ele=999
print("before insert array",arr)

arr.append(0)
for i in range(len(arr)-1,pos-1,-1):
    arr[i]=arr[i-1]
arr[pos]=ele

print(arr)


#deletion of an array element
delete_ele_position=3
for i in range(delete_ele_position,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop()    
print(arr)    
#target of sum of two elements
target_array=array("i",[1,5,6,7,12,18])

target_sum =13
current_sum=0

high=len(arr)-1
low=0
while low  < high:
    current_sum=target_array[low]+target_array[high]
    print(current_sum)
    if current_sum==target_sum:
        print(f"found target element at position {target_array[low]} +{target_array[high]}= {target_sum}")
        break
    elif target_sum > current_sum:
        low+=1
    else:
        high-=1
else:
    print("not found  ")   



#binary search


binary_array= array("i",[1,8,11,14,18,23,31])
search_ele=14
low =0
high=len(binary_array)-1
print(f"array len is {high}")
while low < high:
    mid=(low +high)//2
    
    if binary_array[mid]==search_ele:
        print("found ")
        break
    elif  search_ele > mid :
        low+=1
    else:
        high-=1
else:
    print('not found')     


#container height highest 


arr=array("i",[1,4,5,7,8,9,12])

max_vol=0
ans=0
breadth=0
high=len(arr)-1
low =0
while low < high:
    breadth= high-low
    lht=min(arr[low],arr[high])
    max_vol=breadth *lht
    ans=max(max_vol,ans)

    if arr[low] < arr[high]:
        low+=1
    else:
        high-=1
print(f"highest cap is {ans}")  


#product of all ele except itself

arr_prod=array("i",[1,2,4,6])
n=len(arr_prod)
left_prod=1
right_prod=1
result=[1]*n
print(result)
for i in range(n):
    result[i]=left_prod
    left_prod*=arr_prod[i]


for i in range(n-1,-1,-1):
    result[i]*= right_prod
    right_prod*= arr_prod[i]
print(result)    















