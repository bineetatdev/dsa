
# Day 1 Q2
#This problem requires filtering a list of strings based on two conditions:
#Length Condition: The string's length must be greater than or equal to k.
#Vowel Count Condition: The string must contain at least m vowels.

def filter_strings(lst: list[str],k:int, m:int) -> list[str]:
    return [s for s in lst if len(s) >= k and count_vowels(s) >= m]


def count_vowels(s):
    vowels = set("aeiouAEIOU")  # Set of vowels (both lowercase & uppercase) and using set because it will be O(1), Checking in list will be O(n)
    return sum(1 for char in s if char in vowels)  # Count vowels in string


## Complexity of count_vowels method is O(n)
## Complexity of filter Strings method is O(L . n), where L is the Number of string in list.
## So overall complexity is O(L.n)