# Date and time Jun 17 2024 09:47 am
# @ author : Mesfin Haftu
# """ Merge sort algorithm is a divide and conquer algorithm
#     splits the list into two parts until list with one element and sorts them recursively
# """

from random import randint
from time import perf_counter, process_time

def merge_sort(input_list):
    """
    Merge sort algorithm is a divide and conquer algorithm
    splits the list into two parts until list with one element and sorts them recursively
    :param input_list: list to be sorted
    :return: sorted list
    time complexity: O(nlogn) n times to compare and merge, log(n) times to split
    """
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left_half = input_list[:mid]
        right_half = input_list[mid:]
        
    i = 0
    j = 0
    sorted_list = []
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1
    if i < len(left_half):
        sorted_list.extend(left_half[i:])
    else:
        sorted_list.extend(right_half[j:])
        
    return sorted_list
        
input_list = [randint(1, 1_000_000) for x in range(100_000_000)] # 10 million random numbers between 1 and 1,000,000
# print(input_list)
t1 = perf_counter()
merge_sort(input_list)
print(perf_counter() - t1) # returns elapsed time in seconds(accurate) including sleep and system-wide
print(process_time()) # returns elapsed time in seconds specific to current process.