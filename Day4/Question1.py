# Day4 Q1
# The Minimum Difference Between Highest and Lowest of K Scores problem is a Sliding Window + Sorting problem in DSA

def min_difference(nums, k):
    if k == 1:
        return 0  # If k=1, the difference is always 0 (single element)
    
    nums.sort()  # Sort the array
    min_diff = float('inf')  # Initialize min difference as large number

    # Use sliding window of size k
    for i in range(len(nums) - k + 1):  
        diff = nums[i + k - 1] - nums[i]  # Difference between max & min in window
        min_diff = min(min_diff, diff)  # Update minimum difference

    return min_diff


# Time Complexity: O(n log n) due to sorting

