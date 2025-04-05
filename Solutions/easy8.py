from itertools import combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for k in range(1, n + 1):
            for subset in combinations(nums, k):
                xor = 0
                for num in subset:
                    xor ^= num
                total += xor
        return total
