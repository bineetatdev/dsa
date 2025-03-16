# Day 1 Q1
# Sort tuples by Sum of elements
def sort_by_tuple_sum(lst: list[tuple]) -> list[tuple]:
    return sorted(lst, key=lambda x: sum(x))


## Python internally uses timsort algorithm for sorting
## Time Complexity: O(nlogn)
## Space Complexity: O(n)


