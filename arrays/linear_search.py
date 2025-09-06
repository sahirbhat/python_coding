# # Create an empty array
# array = []

# # Input the number of elements
# n = int(input("Enter the number of elements: "))

# # Take elements at runtime
# print("Enter the elements:")
# for i in range(n):
#     element = input(f"Element {i+1}: ")
#     array.append(element)  # Append each element to the array
# flag=0
# # Print the final array
# print("The array is:", array)
# search_ele=0
# print("enter the ele u want ot search")
# search_ele=input()
# for i in range(len(array)):
#     print(array[i])
#     if array[i] ==search_ele:
#         flag=1
#         break
# if flag==0:
#     print(f"serach {search_ele} element not found ")  
# else:
#     print(f"search element{search_ele} found ")      

# # from array import *

# # arr=array("i",[])
# # arr.append(90)
# # arr.append(91)
# # print(arr)

from array import *
ele=6
flag=0
ar=array("i",[34,78,55,44,33,66,99])
ar1=array('i',[90,90,90])
for i in range(len(ar)):
    if ar[i]==ele:
        flag=1
if flag ==1:
    print("found")
else:
    print("not found")  
ar.append(77) 
print(ar)
ar.pop()  
print(ar)
n=ar.count(34)  
print(n) 
print(ar.reverse())


        

