# binary search

import math
from typing import List

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# given the number (n) find it the n is in the array

def binary_search(arr: List[int], n: int):
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = int(min + math.floor((max - min)/2))

        mid_value = arr[mid]

        if mid_value < n:
            min = mid + 1
            continue
        if mid_value > n:
            max = mid -1
            continue
        if mid_value == n:
            return mid
    
    return -1

if binary_search(primes, 67) != 18:
    raise Exception("should be 18")

if binary_search(primes, 3) != 1:
    raise Exception("should be 1")

if binary_search(primes, 89) != 23:
    raise Exception("should be 23")

if binary_search(primes, 24) != -1:
    raise Exception("should be -1")