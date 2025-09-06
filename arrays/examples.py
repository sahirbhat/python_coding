# from array import *


# arr=array("i",[1,6,7,3,4,7,8,9])
# print(arr)

# # arr.append(666)

# # arr2=sorted(arr)
# # print(arr2)
# #insertion of an array


# ele=999
# position=3
# arr.append(0)




# for i in range(len(arr)-1,position-1,-1):
#     arr[i]=arr[i-1]
# arr[position]=ele
# print(arr)


# #deleetion of an element
# ele_del_position=3
# for i in range((ele_del_position),len(arr)-1):
#     arr[i]=arr[i+1]
# print(arr) 


# #target sum
# arr=sorted(arr)
# target_sum=10
# low=0
# high=len(arr)-1
# current_sum=0

# while low < high:
#     current_sum=arr[low]+arr[high]
#     if target_sum ==current_sum:
#         print(f"found {arr[low],arr[high]}")
#         break

#     elif current_sum  < target_sum:
        
#         low += 1  # Increase the lower pointer
#     else:
#         high -= 1  # Decrease the higher pointer
# else:
#     print(f"No pair found for target sum {target_sum}.")




# #contaianer height

# arr_arr=array("i",[4,7,9,8,4,2])

# high=len(arr_arr)-1
# low=0

# max_cap=0
# ans=0

# while low  < high:
#     width=high-low
#     low_ht=min(arr_arr[low],arr_arr[high])
#     max_cap= low_ht * width
#     ans=max(max_cap,ans)
#     if   arr_arr[low] < arr_arr[high] :
#         low+=1
#     else:
#         high-=1
# print(ans)

# from array import *

# arr_bin_search = array("i", [1, 5, 7, 9, 11, 23, 15, 16])  # Input array
# ele = 16  # Element to search

# # Binary search requires the array to be sorted
# arr_bin_search = sorted(arr_bin_search)

# low = 0
# high = len(arr_bin_search) - 1

# while low <= high:
#     mid = (low + high) // 2  # Find the middle index

#     if arr_bin_search[mid] == ele:
#         print(f"Element {ele} found at index {mid}.")
#         break
#     elif arr_bin_search[mid] > ele:
#         high = mid - 1  # Narrow search to the left half
#     else:
#         low = mid + 1  # Narrow search to the right half
# else:
#     print(f"Element {ele} not found.")
            
    
#binaary serach
from array import *
arr=array("i",[1,4,5,7,9,11,44,66,88])
low =0
high=len(arr)-1

search_ele=11

while low < high:
    mid=(low+high)//2
    if arr[mid]==search_ele:
        print(f" found  {search_ele} at index {mid}")
        break
    if search_ele > mid:
        low+=1
    else:
        high-=1
else:
    print("not found") 


#target sum
from array import *
arr=array("i",[1,4,5,7,9])
low =0
high=len(arr)-1
target_sum=55

while low < high:
    current_sum=arr[low]+arr[high]
    if current_sum ==target_sum:
        print(f"found target sum {target_sum}, at index {low},{high}")
        break

    elif current_sum < target_sum:
        low+=1
    else:
        high-=1
else:
    print("not found") 


#Container_height

from array import *
arr=array("i",[1,4,5,7,9,11,44,66,88])
low =0
high=len(arr)-1
ans=0
max_water=0


while  low < high:
    width=high-low
    lowest_low=min(high,low)
    max_water=width*lowest_low
    ans=max(ans,max_water)

    if arr[low] < arr[high]:
        low+=1
    else:
        high+=1  
print(ans)          


# Reverse a String
# Given a string as a character array, reverse it in-place using two pointers.

str="hello i  m world"
str_list=list(str)

low=0
high=len(str)-1

print(str_list[low],str_list[high])

while low < high:
    str_list[low],str_list[high]=str_list[high],str_list[low]

    high-=1
    low+=1
    rev_str= "".join(str_list)
print(rev_str)  


def str_reverse(s):
    rev=s[::-1]
    print(rev)
    return s ==s[::-1]



my_string="sahir"
if(str_reverse(my_string)):
    print("palidrome")
else:
    print("not plaindrome") 

# Remove Duplicates from Sorted Array   
# 
duplicat_array=array("i",[4,4,8,11,11,11,45,67,89,89,89,123,]) 


arr_original=array("i")
for i in duplicat_array:
    if  not arr_original or   arr_original[-1]!=i:
        arr_original.append(i)
print(arr_original)        













