# Day 6 Q2
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]  # DP table

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill DP table from smaller substrings to larger ones
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index
            if s[i] == s[j]:  # Matching characters
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:  # Exclude one character at a time
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]  # The LPS length for the full string


    # Sort using custom comparator
    nums.sort(key=cmp_to_key(compare))

    # Edge case: If largest number is "0", return "0"
    return "0" if nums[0] == "0" else "".join(nums)


# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing the sorted array

nums = [3, 10, 4]
print(largest_number(nums))  # Output: "9534330"