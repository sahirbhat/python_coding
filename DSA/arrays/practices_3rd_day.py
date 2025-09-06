from array import *

arr=array("i",[1,3,5,7,8,10])
# arr.insert(2,333)
ele=444
loc=4
# arr.append(0)

# for i in range(len(arr)-1,loc-1,-1):
#     arr[i]=arr[i-1]


# arr[loc]=ele
# print("array after insertion")
# print(arr)

#deletion of an array

# del_loc=4

# for i in range(del_loc,len(arr)-1):
#     arr[i]=arr[i+1]
# print("array after Deletion")

# print(arr) 


#target_sum
target_sum=9
low=0

high=len(arr)-1

while low < high:
    current_sum=arr[low]+arr[high]
    if current_sum==target_sum:
        print(f"found {target_sum} at index {low+1}, {high+1}")
        break
    elif target_sum > current_sum:
        low+=1
    else:
        high-=1
else:
    print("Not Found ") 


#Conatiner max water supply


arr_container=array("i",[1,6,7,9,12])
high=len(arr_container)-1
low=0
max_cap=0
ans=0
while low < high:

    width=high-low
    min_ht= min(arr_container[low],arr_container[high])
    max_cap=width * min_ht
    ans=max(max_cap,ans)
    if arr_container[low] < arr_container[high]:

        low+=1
    else:
        high-=1

print(ans) 


#product sum of array elements except itself

product=array("i",[2,4,7])
n=len(product)

result=[1]*n
# print(result)

left_product=1
right_product=1
for i in range(n):
    result[i]=left_product
    left_product*=product[i]

for i in range(n-1,-1,-1):

    result[i]*=right_product
    right_product*=product[i]


print(result)








