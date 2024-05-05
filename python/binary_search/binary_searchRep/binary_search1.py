import math
import binaryTest
from typing import List

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# arr []
# find the mid
# while (compare the mid value with the target)
# if the target is bigger than the mid value this means that the value is not less then the mid
#   so we move the min to mid + 1
# if the target is smaller than mid value, this means that anything more that the mid is invalid gues
#   so we set the max to max = mid -1
# if target == mid value we found our index
# the base case min > max than we need to break. the target in not in the arr
def binary_search(arr: List[int], target: int):
    min = 0
    max = len(arr)

    while not (max < min):
        mid = int(min + math.floor((max - min)/2))
        mid_value = arr[mid]

        if mid_value > target:
            max = mid -1
            continue

        if mid_value < target:
            min = mid + 1
            continue

        if mid_value == target:
            return mid
    
    return -1

binaryTest.test(binary_search)