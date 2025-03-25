# Day11 Q2
# Given a string word and an abbreviation abbr, return True if word matches abbr. Otherwise, return False.


def valid_word_abbreviation(word, abbr):
    i, j = 0, 0  # Pointers for word and abbr
    
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():  # If abbr[j] is a digit
            if abbr[j] == '0':  # Leading zero check
                return False  

            num = 0
            while j < len(abbr) and abbr[j].isdigit():  # Extract full number
                num = num * 10 + int(abbr[j])
                j += 1
            
            i += num  # Move i forward by extracted number

        else:  # If it's a letter
            if i >= len(word) or word[i] != abbr[j]:  # Must match exactly
                return False
            i += 1
            j += 1

    return i == len(word) and j == len(abbr)  # Ensure both are fully processed


# Time Complexity O(n)