'''
3264. Final Array State After K Multiplication Operations I

2024.08.25 Sunday 13:10
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for _ in range(k):
            min_value = nums[0]
            index = 0
            for idx, n in enumerate(nums):
                if n < min_value:
                    min_value = n
                    index = idx
            nums[index] = nums[index] * multiplier
        return nums



if __name__ == "__main__":
    obj = Solution()
    assert obj.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2) == [8,4,6,5,6]
    assert obj.getFinalState(nums = [1,2], k = 3, multiplier = 4) == [16,8]
