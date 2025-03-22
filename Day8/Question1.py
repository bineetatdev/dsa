# Day8 Q1
#You are given an array nums where each element represents the maximum number of steps you can jump forward from that position. Return True if you can reach the last index, otherwise return False.
def can_jump(nums):
    max_reach = 0  # How far we can jump
    for i in range(len(nums)):
        if i > max_reach:  # If current index is unreachable
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:  # If we can reach the last index
            return True
    return True

nums = [2, 3, 1, 1, 4]
print(can_jump(nums))  # Output: True
# Time complexity O(n)
