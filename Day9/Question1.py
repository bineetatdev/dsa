# Day9 Q1
# Longest uncommon subsequence
#Given a list of strings strs, return the length of the longest uncommon subsequence. If no uncommon subsequence exists, return -1.


def is_subsequence(s1, s2):
    """Check if s1 is a subsequence of s2."""
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)

def find_LUS_length(strs):
    strs.sort(key=len, reverse=True)  # Sort strings by length (longest first)
    
    for i, word in enumerate(strs):
        uncommon = True
        for j, other in enumerate(strs):
            if i != j and is_subsequence(word, other):
                uncommon = False
                break
        if uncommon:
            return len(word)
    
    return -1

# Time complexity O(n2)