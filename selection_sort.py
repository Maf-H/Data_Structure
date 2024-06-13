# Date and Time Jun 13 2024 10:23 pm
# @ author : Mesfin Haftu

# Selection sort algorithm to sort numbers in ascending and descending order
# Time complexity: O(n^2)
from random import randint

def find_smallest(input_list):
    """ this function used to find the smallest element in the list """
    smallest = input_list[0]
    smallest_index = 0
    
    for i in range(1, len(input_list)):
        if input_list[i] < smallest:
            smallest = input_list[i]
            smallest_index = i
    return smallest_index

def selection_sort(input_list):
    ascending = []
    descending = []
    
    for i in range(len(input_list)):
       smallest = find_smallest(input_list)
       smallest_value = input_list.pop(smallest)
       ascending.append(smallest_value) # pop receives index and returns value @index
       descending.insert(0, smallest_value) # pushes previous values to the right and inserts the value to the first index
    return ascending, descending

unsorted_list = [randint(1, 100) for x in range(10)]
print(f"""{unsorted_list} 
==================================================""")
asc, desc = selection_sort(unsorted_list)
print(asc, "\n", desc)