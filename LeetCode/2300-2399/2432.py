'''
2342. Max Sum of a Pair With Equal Sum of Digits

2022.07.17 Sunday 14:15
'''
from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits_sums = defaultdict(list)
        for n in nums:
            digits_total = sum([int(i) for i in str(n)])
            digits_sums[digits_total].append(n)

        max_v = -1
        for k, vs in digits_sums.items():
            lens = len(vs)
            if lens>1:
                max_v = max(max_v, sum(sorted(vs)[-2:]))
        return max_v


if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumSum(nums = [18,43,36,13,7])==54
    assert obj.maximumSum(nums = [10,12,19,14])==-1
