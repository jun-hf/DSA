import math
from typing import List
import binaryTest

def binary_search(arr: List[int], target: int):
    min = 0
    max = len(arr) -1 

    return recur_bs(min, max, arr, target)

def recur_bs(min: int, max: int, arr: List[int], target: int):
    if min > max:
        return -1
    mid = int(min + math.floor((max -min)/2))
    mid_val = arr[mid]
    if mid_val == target:
        return mid
    if mid_val < target:
        return recur_bs(mid +1, max, arr, target)
    if mid_val > target:
        return recur_bs(min, mid-1, arr, target)
    
binaryTest.test(binary_search)