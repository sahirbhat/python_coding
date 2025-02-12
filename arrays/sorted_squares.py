def sorted_squares(nums):
    n = len(nums)
    result = [0] * n  # Result array of size n
    low, high = 0, n - 1  # Initialize two pointers
    position = n - 1  # Start filling result from the last position

    while low <= high:
        if nums[low] ** 2 > nums[high] ** 2:
            result[position] = nums[low] ** 2
            low += 1  # Move the low pointer to the right
        else:
            result[position] = nums[high] ** 2
            high -= 1  # Move the high pointer to the left
        position -= 1  # Move to the next position in the result array

    return result

# Example usage
nums = [-7, -3, 2, 3, 11]
print(sorted_squares(nums)) 