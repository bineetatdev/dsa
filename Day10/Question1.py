# Day10 Q1
# Given an integer array nums, return True if there exists a continuous subarray of at least size 2 whose sum is a multiple of k. Otherwise, return False.
def check_subarray_multiple(nums, k):
    """Returns True if continuous subarray of size >= 2 exists with sum multiple of k"""
    n = len(nums)
    if n < 2:
        return False
    
    # Check all possible subarrays of length >= 2
    for i in range(n):
        curr_sum = nums[i]
        for j in range(i + 1, n):
            curr_sum += nums[j]
            if curr_sum % k == 0:
                return True
    return False

nums = [23, 2, 4, 6, 7]
k = 6
print(check_subarray_multiple(nums, k))  # Output: True

# Time Complexity O(n)