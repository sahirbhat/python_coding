arr = [1, 9, 7, 2, 23, 56, 67, 34, 7, 9]
search_ele = 67
arr = sorted(arr)  # Binary search requires a sorted array
print(f"Sorted array: {arr}")

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2  # Find the middle index
    if arr[mid] == search_ele:
        print(f"Found element {search_ele} at index {mid}")
        break
    elif search_ele > arr[mid]:  # Element is in the right half
        low = mid + 1
    else:  # Element is in the left half
        high = mid - 1
else:
    print("Element not found")
