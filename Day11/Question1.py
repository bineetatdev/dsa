# Day11 Q1
# Given a sorted array nums, modify it in-place so that each element appears at most twice, maintaining relative order. Return the new length.

def remove_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)  # Already meets criteria

    i = 2  # Start from the 3rd position since the first two can remain

    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:  # Ensure at most two occurrences
            nums[i] = nums[j]
            i += 1  # Move to next position

    return i  # New valid length

nums = [1, 1, 1, 2, 2, 3]
new_length = remove_duplicates(nums)
print(new_length)  # Output: 5

# Time Complexity O(n)