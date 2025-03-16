# Day 2 Q1
# Length of the last word.
# You are given a sentences that contains words and spaces. Task is to find the length of the last word
# in the sentences.
def length_of_last_word(s: str) -> tuple:
    words = s.split()
    if not words:
        return ("",0)
    last_word = words[-1]
    return last_word,len(last_word)
    

w,l = length_of_last_word(" fly me to the moon ")
print('The last word is "{}", which has {} letters.'.format(w,l))

## Splitting the string s.split is having O(n) complexity
## Accessing the last word. Time Complexity: O(1)
## Finding the length of the word O(1) . So total time complexity is O(n)




