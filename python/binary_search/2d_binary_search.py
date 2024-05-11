import unittest
import math
from typing import List

def search(arr: List[int], target: int):
    row_min = 0
    row_max = len(arr) -1

    targetInRow = -1
    isInRange = False
    while row_min <= row_max:
        mid_row = int(row_min + math.floor((row_max -row_min)/2))
        print(mid_row)

        if arr[mid_row][0] <= target and arr[mid_row][len(arr[mid_row]) -1] >= target:
            isInRange = True
            targetInRow = mid_row
            break

        if target < arr[mid_row][0]:
            row_max = mid_row -1
        
        if target > arr[mid_row][len(arr[mid_row]) -1]:
            row_min = mid_row +1
    if not isInRange:
        return -1
    
    column_min = 0
    column_max = len(arr[targetInRow]) -1

    while column_min <= column_max:
        mid = int(column_min + math.floor((column_max - column_min)/2))
        mid_value = arr[targetInRow][mid]

        if mid_value == target:
            return [targetInRow, mid]
        if mid_value < target:
            column_min = mid +1
        if mid_value > target:
            column_max = mid -1
    
    return -1

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

class TestSearch(unittest.TestCase):
    def test_1(self):
        self.assertEqual(search(matrix, 1), [0, 0])
    def test_3(self):
        self.assertEqual(search(matrix, 3), [0, 1])
    def test_5(self):
        self.assertEqual(search(matrix, 5), [0, 2])
    def test_7(self):
        self.assertEqual(search(matrix, 7), [0, 3])
    def test_10(self):
        self.assertEqual(search(matrix, 10), [1, 0])
    def test_11(self):
        self.assertEqual(search(matrix, 11), [1, 1])
    def test_16(self):
        self.assertEqual(search(matrix, 16), [1, 2])
    def test_20(self):
        self.assertEqual(search(matrix, 20), [1, 3])
    def test_23(self):
        self.assertEqual(search(matrix, 23), [2, 0])
    def test_30(self):
        self.assertEqual(search(matrix, 30), [2, 1])
    def test_34(self):
        self.assertEqual(search(matrix, 34), [2, 2])
    def test_60(self):
        self.assertEqual(search(matrix, 60), [2, 3])
    def test_88(self):
        self.assertEqual(search(matrix, 88), -1)

if __name__ == "__main__":
    unittest.main()