# Day9 Q2
# Find K closest element
# Given a sorted array arr and a target value x, return the K closest elements to x. The result should be sorted in ascending order.

import bisect

def find_closest_elements(arr, k, x):
    # Find the closest index to 'x' using binary search
    right = bisect.bisect_left(arr, x)
    left = right - 1

    # Expand two pointers to find the k closest elements
    while k > 0:
        if left < 0:
            right += 1
        elif right >= len(arr) or (x - arr[left] <= arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1

    return arr[left + 1:right]  # Extract the subarray

# Binary Search (bisect_left)	O(log n)
# Expanding Pointers	O(k)
# Total	O(log n + k)