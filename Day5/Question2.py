# Day 5 Q2
# Largest number
# Given an array of non-negative integers nums, arrange them to form the largest possible number.

from functools import cmp_to_key

def largest_number(nums):
    # Convert numbers to strings
    nums = list(map(str, nums))

    # Custom sorting: Compare concatenated strings
    def compare(x, y):
        return -1 if x + y > y + x else 1  # Sort in descending order

    # Sort using custom comparator
    nums.sort(key=cmp_to_key(compare))

    # Edge case: If largest number is "0", return "0"
    return "0" if nums[0] == "0" else "".join(nums)


# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing the sorted array

nums = [3, 10, 4]
print(largest_number(nums))  # Output: "9534330"