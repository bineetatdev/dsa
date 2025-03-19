# Day5 Q1
# Find peak Element
# A peak element in an array is an element that is strictly greater than its neighbors. Given an array nums, return any peak element's index.
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:  # Peak is on left side
            right = mid
        else:  # Peak is on right side
            left = mid + 1
    
    return left  # Peak index

nums = [8, 2, 1, 3, 5, 6, 4]    
print(find_peak_element(nums))

# Time complexity O(logn)