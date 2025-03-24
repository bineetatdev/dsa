# Day10 Q2
# Given two integers low and high, return a list of all numbers in the range [low, high] that have sequential digits. The numbers should be sorted in increasing order.

def sequential_digits(low, high):
    result = []
    for i in range(1, 10):  # Start with single-digit numbers
        num = i
        next_digit = i + 1
        while num <= high and next_digit <= 9:
            num = num * 10 + next_digit
            if low <= num <= high:
                result.append(num)
            next_digit += 1
    return sorted(result)

# Time Complexity: O(1) as the range is limited
# Space Complexity: O(1) for storing the result

low = 100
high = 300
print(sequential_digits(low, high))  # Output: [123, 234]

