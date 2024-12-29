from array import *


arr=array("i",[1,6,7,3,4,7,8,9])
print(arr)

# arr.append(666)

# arr2=sorted(arr)
# print(arr2)
#insertion of an array


ele=999
position=3
arr.append(0)




for i in range(len(arr)-1,position-1,-1):
    arr[i]=arr[i-1]
arr[position]=ele
print(arr)


#deleetion of an element
ele_del_position=3
for i in range((ele_del_position),len(arr)-1):
    arr[i]=arr[i+1]
print(arr) 


#target sum
arr=sorted(arr)
target_sum=10
low=0
high=len(arr)-1
current_sum=0

while low < high:
    current_sum=arr[low]+arr[high]
    if target_sum ==current_sum:
        print(f"found {arr[low],arr[high]}")
        break

    elif current_sum  < target_sum:
        
        low += 1  # Increase the lower pointer
    else:
        high -= 1  # Decrease the higher pointer
else:
    print(f"No pair found for target sum {target_sum}.")




#contaianer height

arr_arr=array("i",[4,7,9,8,4,2])

high=len(arr_arr)-1
low=0

max_cap=0
ans=0

while low  < high:
    width=high-low
    low_ht=min(arr_arr[low],arr_arr[high])
    max_cap= low_ht * width
    ans=max(max_cap,ans)
    if   arr_arr[low] < arr_arr[high] :
        low+=1
    else:
        high-=1
print(ans)

from array import *

arr_bin_search = array("i", [1, 5, 7, 9, 11, 23, 15, 16])  # Input array
ele = 16  # Element to search

# Binary search requires the array to be sorted
arr_bin_search = sorted(arr_bin_search)

low = 0
high = len(arr_bin_search) - 1

while low <= high:
    mid = (low + high) // 2  # Find the middle index

    if arr_bin_search[mid] == ele:
        print(f"Element {ele} found at index {mid}.")
        break
    elif arr_bin_search[mid] > ele:
        high = mid - 1  # Narrow search to the left half
    else:
        low = mid + 1  # Narrow search to the right half
else:
    print(f"Element {ele} not found.")
            
    
















