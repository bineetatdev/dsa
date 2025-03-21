# Day 7 Q2
# Maximum Gap
# Given an unsorted array of numbers, find the maximum difference between two successive elements after sorting the array.

import math

def maximum_gap(nums):
    if len(nums) < 2:
        return 0  # No gap possible

    # Step 1: Find min and max values
    min_val, max_val = min(nums), max(nums)
    n = len(nums)

    if max_val == min_val:
        return 0  # All elements are the same

    # Step 2: Compute bucket size and number of buckets
    gap = math.ceil((max_val - min_val) / (n - 1))
    num_buckets = (max_val - min_val) // gap + 1
    
    # Step 3: Initialize buckets
    buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]

    # Step 4: Place elements in their respective buckets
    for num in nums:
        index = (num - min_val) // gap
        buckets[index][0] = min(buckets[index][0], num)
        buckets[index][1] = max(buckets[index][1], num)

    # Step 5: Compute maximum gap between non-empty buckets
    max_gap, prev_max = 0, min_val

    for b_min, b_max in buckets:
        if b_min == float('inf'):  # Empty bucket
            continue
        max_gap = max(max_gap, b_min - prev_max)
        prev_max = b_max

    return max_gap

nums = [3, 6, 9, 1]
print(maximum_gap(nums))

# Time complexity   
    # Finding Min Max O(n)
    # Bucket Sorting O(n)
    # Finding Max Gap O(n)
    # Finally O(n)
