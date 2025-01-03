def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Left pass: Accumulate product of elements to the left of the index
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

 
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example usage
nums = [1, 2, 3, 4]
output = product_except_self(nums)
print(output)  # Output: [24, 12, 8, 6]



def product(nums):
    n=len(nums)
    result=[1]*n
    left_prod=1
    right_prod=1
    for i in range(n):
        result[i]=left_prod
        left_prod*=nums[i]

    for i in range(n-1,-1,-1):
        result[i]*=right_prod
        right_prod*=nums[i]

    print( result)



nums = [1, 2, 3, 4]



product(nums)