# Date and Time Jun 13 2024 03:56 pm
# @ author : Mesfin Haftu
from random import randint
from time import perf_counter, process_time
def quick_sort(input_list):
    """
    Quick sort algorithm is a divide and conquer algorithm
    splits the list into two(less than the pivot, and greater than the pivot) parts and sorts them recursively
    :param input_list: list to be sorted
    :return: sorted list
    time complexity: O(nlogn) n times to compare and split, log(n) times to merge and sort
    """
    if len(input_list) < 2:
        return input_list
    else:
        pivot = input_list[0]
        left = [x for x in input_list[1:] if x <= pivot]
        right = [x for x in input_list[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
t1 = perf_counter()  
input_list = [randint(1, 1_000_000) for x in range(10_000_000)] # 10 million random numbers between 1 and 1,000,000
# print(input_list)
quick_sort(input_list)
print(perf_counter() - t1) # returns elapsed time in seconds(accurate) including sleep and system-wide
print(process_time()) # returns elapsed time in seconds specific to current process.
