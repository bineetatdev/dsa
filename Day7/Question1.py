# Day7 Q1
# Valid triangles
# Given an array of integers representing side lengths, find the number of valid triangles that can be formed.
def count_valid_triangles(nums):
    nums.sort()  # Step 1: Sort the sides
    n = len(nums)
    count = 0

    # Step 2: Fix the largest side (c) and use two pointers for (a, b)
    for c in range(n - 1, 1, -1):  # Start from the largest side
        left, right = 0, c - 1
        while left < right:
            if nums[left] + nums[right] > nums[c]:  # Valid triangle
                count += (right - left)  # All pairs (left to right-1) are valid
                right -= 1  # Move right pointer left to find more
            else:
                left += 1  # Move left pointer right (increase sum)

    return count


nums = [2, 2, 3, 4] 
print(count_valid_triangles(nums))


# Time complexity Sorting - O(nlogn) Two-Pointer Search - O(n2). Final is O(n2)