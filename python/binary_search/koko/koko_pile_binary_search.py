import math
def k_banana(arr, h):
    l, r = 0, max(arr)
    res = max(arr)
    while l <= r:
        k = (l + r) // 2
        time_taken = 0
        for p in arr:
            time_taken += math.ceil(p/k)

        if time_taken <= h:
            res = min(res, k)
            r = k -1
        if time_taken > h:
            l = k +1
    return res

import unittest
class TestKBanana(unittest.TestCase):
    def test_8h(self):
        self.assertEqual(k_banana([3,6,7,11], 8), 4)
    def test_5h(self):
        self.assertEqual(k_banana([30,11,23,4,20], 5), 30)
    def test_6h(self):
        self.assertEqual(k_banana([30,11,23,4,20], 6), 23)