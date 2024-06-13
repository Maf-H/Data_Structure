# Date and Time Jun 13 2024 04:56 pm
# @ author : Mesfin Haftu
"""
Recursive functions for some operations
"""

from random import randint
def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num - 1)
    
def array_adder(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + array_adder(nums[1:])
def array_counter(nums):
    if nums == []:
        return 0
    else:
        return 1 + array_counter(nums[1:])
def max_of_array(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0], max_of_array(nums[1:]))

arr = [x for x in range(1, 101)] 
random_array = [randint(1, 100) for x in range(10)]
print(array_adder(arr))
print(fact(5))
print(array_counter(arr))
print(random_array)
print(max_of_array(random_array))

