# Day3 Q1
#
def product_except_self(nums:list[int])->list[int]:
    p_list = []
    for x in range(len(nums)):
        p = 1
        for y in range(len(nums)):
            if nums[x]!=nums[y]:
                p=p*nums[y]
            else:
                continue
        p_list.append(p)
    return p_list

# Time complexity: O(n^2)
# Space Complexity: O(n)

def product_except_self_optimized(nums:list[int])->list[int]:
    n = len(nums)
    output = [1] * n  # Initialize result array with 1s

    # Compute left products
    left_product = 1
    for i in range(n):
        output[i] = left_product  # Store left product
        left_product *= nums[i]   # Update left product

    # Compute right products and final result
    right_product = 1
    for i in range(n - 1, -1, -1):  # Reverse traversal
        output[i] *= right_product  # Multiply with right product
        right_product *= nums[i]    # Update right product

    return output

# Time complexity: O(n)
# Space Complexity: O(1)

nums = [1,2,3,4]
print(product_except_self(nums))
print(product_except_self_optimized(nums))