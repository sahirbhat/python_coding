# # # from array import *

# # # arr=array('i',[22,44,55,66,77,88,6])
# # # print(arr)

# # # inserted_element=99
# # # target=2
# # # arr.append(0)

# # # for i in range(len(arr)-1,target-1,-1):
# # #     arr[i] = arr[i-1]


# # # arr[target]=inserted_element
# # # print(arr)
# # # arr.insert(1,444)
# # # print(arr)

# # # #delete of an element

# # # delete_pos=3
# # # for i in range(delete_pos-1,len(arr)-1):
# # #     arr[i] = arr[i+1]
# # # print(arr)    
    
# # # for i in range(len(arr)-1):
# # #     print(arr[i])    


# # # # arr2=['i',45,67,8,8,45,67,33,6,2,5,2]
# # # # temp=0
# # # # for i in range(0,len(arr2)-1):
# # # #     for j in range(i,len(arr2)-1):
# # # #         if arr2[j] > arr[j]+1:   
# # # #             temp=arr2[j]
# # # #             arr2[j]=arr2[j]+1
# # # #             arr2[j]+1=temp
# # # # print(arr2) 


# # # arr2 = [45, 67, 8, 8, 45, 67, 33, 6, 2, 5, 2]
# # # for i in range(len(arr2)-1):
# # #     for j in range(len(arr2)-i-1):
# # #         if arr2[j] > arr2[j+1]:  # Swap if elements are out of order
# # #             arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

# # # print(arr2)  # [2, 2, 5, 6, 8, 8, 33, 45, 45, 67, 67]

# # from array import *

# # arr_roll=array('i',[77,55,66,77,88,99,34,66])
# # arr_roll.append(0)
# # # arr=array('i',[22,44,55,66,77,88,6])
# # print(arr_roll)
# # target=3
# # inserted_ele=420


# # for i in range(len(arr_roll)-1,target-1,-1):
# #     arr_roll[i]=arr_roll[i-1]


# # arr_roll[target-1] =inserted_ele  
# # print(arr_roll) 

# # #delete an elee

# # delete_ele_pos=3

# # for i in range(delete_ele_pos-1,len(arr_roll)-1):
# #     arr_roll[i]=arr_roll[i+1]
# # arr_roll.pop() 
# # print(arr_roll) 

# # arr=array('i',[22,44,1,7,7,3,0,-1,-45,55,66,77,88,6])

# # for i  in range(0,len(arr)):
# #     for j in range(len(arr)-i-1):
# #         if arr[j]>arr[j+1]:
# #             arr[j],arr[j+1]=arr[j+1],arr[j]
# # print(arr)  

# # # reverse of an array
# # print("-----------------------reverse")
# # arr_rev=array('i',[5,8,1,6,45,67,88,99,23])


# # for i in arr_rev[::-1]:

# #     print(i)
# # # print(len(arr_rev))

# # # for i in range(0,len(arr_rev),1):
# # #     print(arr_rev[-i]) 

# # from array import array

# # arr_rev = array('i', [5, 8, 1, 6, 45, 67, 88, 99,10001, 23])

# # # Reverse and print array elements
# # for i in range(len(arr_rev) - 1, -1, -1):  # Start from the last index and go to 0
# #     print(arr_rev[i])

# # max=0
# # second_max=0

# # # for i in range(0,len(arr_rev)) :
# # #     if arr_rev[i]>max:
# # #         max=arr_rev[i]
        
# # #     if arr_rev[i] < max or arr_rev[i] > second_max:
# # #         second_max=arr_rev[i]  

# # # print("higehst")        
# # # print(max,second_max)  
# # list1=[34,86,90,4,56,34,1]  
# # max=0
# # sec_max=0
# # for i  in list1:
# #     if i >max:
        
# #         sec_max=max 
# #         max=i
# #     elif i > sec_max or i !=max:
# #         sec_max=i 
# # print(max,sec_max)  
# # list1 = [34, 86, 90, 4, 56, 34, 1]

# # max = float('-inf')  # Initialize max with the smallest possible value
# # sec_max = float('-inf')  # Initialize sec_max with the smallest possible value

# # for i in list1:
# #     if i > max:
# #         sec_max = max  # Update sec_max before updating max
# #         max = i
# #     elif i > sec_max and i != max:  # Check for second max
# #         sec_max = i

# # print(f"Maximum: {max}, Second Maximum: {sec_max}")

# # #insert elemnt into an array

# # array_inserted=array('i',[87,89,45,2,8,9,12])

# # array_inserted.append(0)
# # target_pos=3
# # element_ins=1000

# # #array inserted 
# # print(array_inserted)
# # for i in range(len(array_inserted)-1,target_pos-1,-1):
# #     array_inserted[i]=array_inserted[i-1]



# # array_inserted[target_pos]=element_ins


# # print(array_inserted)


# # # array_inserted.append(1,9000)

# # #delete of an element
# # position_del=3
# # for i in range(position_del-1,len(array_inserted)-1):
# #     array_inserted[i]=array_inserted[i+1]
# # array_inserted.pop()    
# # print(array_inserted)


# # for i in range(len(array_inserted)-1):
# #     for j  in range(len(array_inserted)-i-1):
# #         if array_inserted[j]>array_inserted[j+1]:
# #             array_inserted[j],array_inserted[j+1]=array_inserted[j+1],array_inserted[j]
# # print(f"sored of array is{array_inserted}")  


# # list_find=[23,67,89,44,33,8]

# # max_1=0
# # max_2=0

# # for i in  list_find:
# #     if i > max_1:
# #         max_2=max_1
# #         max_1=i
# #     elif i > max_2 and max_2!=max_1:
# #         max_2=i 

# # print(f"two highest ele in list is{max_1},{max_2}") 

# # for i in array_inserted[::-1]:
# #     print(i, end=" ")


# # # Move All Zeroes to the End
# # print("xeroes on the end")
# # input=[0, 1, 9, 8, 0, 2, 0, 6]
# # n=len(input)
# # print(n)
# # arr_index=0
# # for i in range(n):
# #     if input[i] !=0:
# #         input[i],input[arr_index]=input[arr_index],input[i]
# #         arr_index+=1
# # print(input)    


# # arr = [1, 2, 3, 4, 5]

# # print(arr[2:]+ arr[:2])
# from array import *
# arr=array("i",[56,89,12,33,45,67,89,90,23])
# print(arr)
# ele_ins=90
# position=3

# arr.append(0)
# for i in range(len(arr)-1,position-1,-1):
#     arr[i]=arr[i-1]


# arr[position] =ele_ins    
# print(arr)  

# delete_position=4

# for i in range(delete_position-1,len(arr)-1):
#     arr[i]=arr[i+1]
# print(arr) 
# sum=0
# for   i in  arr:
#     sum+=i
# print(sum) 
# max1=0
# max2=0
# for i in arr:
#     if i > max1:
#         max2,max1=max1,i
#     elif i >max2 and max2!=max1:  
#         max1=i
# print(max1,max2) 
# ele=89
# flag=0
# try:
#     for i in arr:
#         if i == ele:
#             flag=1
#             break
# except Exception as e:
#     print(f"error coocured ",e)           


# if flag==1:
#     print("found")
# else:
#     print("not found")   

# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1] :
#             arr[j],arr[j+1]=arr[j+1],arr[j]  
# print(f"sorted array is  {arr}")



# Binary Search
# def binary_search(array, search_ele):
#     low = 0
#     high = len(array) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         # Check if element is at mid
#         if array[mid] == search_ele:
#             return mid
#         # If element is smaller than mid, search the left half
#         elif array[mid] > search_ele:
#             high = mid - 1
#         # If element is larger than mid, search the right half
#         else:
#             low = mid + 1

#     return -1  # Element not found

# # Input a sorted array and element to search
# array = [10, 20, 30, 40, 50]  # Must be sorted
# search_ele = 30
# result = binary_search(array, search_ele)

# if result != -1:
#     print(f"Element {search_ele} found at index {result}.")
# else:
#     print(f"Element {search_ele} not found.")

# from array import *
# arr=array("i",[99,45,23,1,67,99,33,2])
# print(arr)
# # for i in range(len(arr)):
# #     for j in range(len(arr)-i-1):
        
# #         if arr[j] > arr[j+1] :
# #             arr[j],arr[j+1]=arr[j+1],arr[j]
# # print(arr) 

# # for i in arr[::-1]:
# #     print( i ,end=" ")
# # ele=333
# # position=3
# # arr.append(0)
# # for i in range(len(arr)-1,position-1):   
# #     arr[i]=arr[i-1] 
# # # arr[position-1]=ele 
# # print(arr)  
# #  #delete
# # postion_del=3
# # for i in range(postion_del-1,len(arr)-1):
# #     arr[i]=arr[i+1]
# # print(arr)    
 
# arr_sorted=array("i",[1,5,7,9,34,65])
# ele=7
# flag=0
# low=0

# high=len(arr_sorted)-1
# while low < high:
#     mid = (low+high) // 2
#     if arr[mid]==ele:
#          flag=1
#          break
#     elif arr[mid] > ele:
#         high=mid-1
#     else:
#         mid =mid+1        
    
# if flag==1:
#     print("found") 
# else:
#     print("not found")  
# 
from array import *
arr = array("i", [3, 5, 7, 8, 9])
high = len(arr) 
print(high)  

from array import *

arr=array("i",[1,6,9,3,4,7])
target_sum=10

low=0


high = len(arr)-1 
for i in range(len(arr)-1):
    if arr[i] + arr[high]==target_sum:
        print(arr[low],arr[high])
        print(f"found{target_sum}: ",arr[i],arr[high]) 
        break
    else:
        
        high-=1


#reverse of an araay using pointers 

arr_rev=array("i",[67,24,6,90,1,3,1])

low=0

high=len(arr_rev)-1

while low < high:
    arr_rev[high],arr_rev[low]=arr_rev[low],arr_rev[high]

    low+=1
    high-=1
print("reversed array",arr_rev)    



def valid_palindrome(s):
    # Compare the string with its reverse
    return s == s[::-1]

str_s = "madam"

if valid_palindrome(str_s):
    print("Palindrome")
else:
    print("Not a palindrome")
   