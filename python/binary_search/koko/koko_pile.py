from typing import List

def k_banana(piles: List[int], h: int):
    amount_of_k = -1
    for k in range(1, max(piles) +1):
        if h >= eat_duration(piles, k):
            amount_of_k = k
            break
    
    return amount_of_k
    
def eat_duration(piles: List[int], k: int):
    h = 0
    for i in piles:
        h += eat_pile(i, k)
    return h

def eat_pile(amount: int, k: int):
    h = amount // k
    if (amount % k != 0):
        h +=1
    return h

import unittest
class TestKBanana(unittest.TestCase):
    def test_8h(self):
        self.assertEqual(k_banana([3,6,7,11], 8), 4)
    def test_5h(self):
        self.assertEqual(k_banana([30,11,23,4,20], 5), 30)
    def test_6h(self):
        self.assertEqual(k_banana([30,11,23,4,20], 6), 23)