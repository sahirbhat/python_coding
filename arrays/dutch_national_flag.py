# def sort_colors(arr):
#     low, mid, high = 0, 0, len(arr) - 1
    
#     while mid <= high:
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             low += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:  # arr[mid] == 2
#             arr[mid], arr[high] = arr[high], arr[mid]
#             high -= 1

#     return arr

# # Example
# nums = [2, 0, 2, 1, 1, 0]
# sorted_nums = sort_colors(nums)
# print("Sorted Colors:", sorted_nums)

from array import array

def sort_number_color(arr):
    arr = list(arr)  # Convert the array to a list for processing
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    arr = array("i", arr)  # Convert back to array if needed
    print(arr)

# Create an array and pass it to the function
arr = array("i", [2, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1])
sort_number_color(arr)
