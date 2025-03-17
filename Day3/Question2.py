# Day3 Q2
# Longest substring without repeating characters

def length_of_longest_substring(s: str) -> int:
    char_set = set()  # To store unique characters in the window
    left = 0  # Left pointer of the sliding window
    max_length = 0  # Store max length of unique substring

    for right in range(len(s)):  
        while s[right] in char_set:  # If duplicate found, shrink window
            char_set.remove(s[left])
            left += 1  

        char_set.add(s[right])  # Add the new character
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length

# Time complexity: O(n)
# Space Complexity: O(min(m,n)), where m is the size of the character set (constant 26 for lowercase English letters)

s = "abcabcbb"
print(length_of_longest_substring(s))