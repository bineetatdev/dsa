
# Day 2 Q2
# Find first and last postions of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
def find_first_and_last(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1,-1]
    left = 0
    right = len(nums) - 1
    first = -1
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [first,last]



nums=[5,7,7,8,8,8,8,10]
target=7
print(find_first_and_last(nums,target))

## Complexity of find_first_and_last method is O(logn)

