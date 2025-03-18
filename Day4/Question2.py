# Day4 Q2
# The Minimum Size Subarray Sum is a classic Sliding Window problem in DSA

def min_subarray_len(target, nums):
    left = 0  # Left pointer
    total = 0  # Current sum
    min_length = float('inf')  # Store minimum length

    for right in range(len(nums)):
        total += nums[right]  # Expand window by adding nums[right]

        while total >= target:  # If sum is enough, shrink window
            min_length = min(min_length, right - left + 1)  # Update min length
            total -= nums[left]  # Remove leftmost element
            left += 1  # Move left pointer forward

    return min_length if min_length != float('inf') else 0  # If no subarray found, return 0


# Time complexity: O(n)
# Space Complexity: O(1)


