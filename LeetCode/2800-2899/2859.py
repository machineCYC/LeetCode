'''
2859. Sum of Values at Indices With K Set Bits

2023.09.17 Sunday 23:24
'''
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        cnt = 0
        for idx, n in enumerate(nums):
            bit_n = "{0:b}".format(idx)
            if len([i for i in bit_n if i == "1"]) == k:
                cnt += n
        return cnt


if __name__ == "__main__":
    obj = Solution()
    assert obj.sumIndicesWithKSetBits(nums = [4,3,2,1], k = 2) == 1
    assert obj.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1) == 13