from array import *

arr = array("i", [1, 6, 9, 3, 4, 7])
target_sum = 10

# Sort the array for the two-pointer technique
arr = sorted(arr)

low = 0
high = len(arr) - 1

# Two-pointer logic
while low < high:
    current_sum = arr[low] + arr[high]
    if current_sum == target_sum:
        print(f"Found pair for target sum {target_sum}: {arr[low]}, {arr[high]}")
        break
    elif current_sum < target_sum:
        low += 1  # Increase the lower pointer
    else:
        high -= 1  # Decrease the higher pointer
else:
    print(f"No pair found for target sum {target_sum}.")


# arr2=array("i",[89,45,67,56,1,4,6])
# arr2=sorted(arr2)

# high=len(arr2)-1
# low=0
# target_sum=7
# while low < high:
#     current_sum=arr2[low]+arr2[high]
#     if current_sum ==target_sum:
#         print(f"found target sum {target_sum},{arr2[low]},{arr2[high]}")
#         break
#     elif current_sum < target_sum:
#         low+=1
#     else:
#         high-=1
# else:
#     print("not found ")        


from array import *
import time
arr=array("i",[77,45,23,78,1,2,3,90])
arr=sorted(arr)
print(arr)

low=0
high=len(arr)-1
print(high)
target_sum=92
start=time.time()
print(start)
while low < high:
    current_sum=arr[low]+arr[high]
    if current_sum ==target_sum:
        print(f"found target sum {target_sum},{arr[low],arr[high]}")
        break
    elif current_sum < target_sum:
        low+=1
    else:
        high-=1
else:
    print("not found")  
end_time=time.time() 
print(f"time taken = {end_time-start}")             
