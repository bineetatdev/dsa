# Day6 Q1
def length_of_longest_substring_two_distinct(s):
    left = 0  # Left pointer of the window
    char_count = {}  # Stores frequency of characters in the window
    max_length = 0  # Track max substring length

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1  # Add right char

        # If more than 2 distinct characters, shrink from left
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]  # Remove char if count is zero
            left += 1  # Move left pointer

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length