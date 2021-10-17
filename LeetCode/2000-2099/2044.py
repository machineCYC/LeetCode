'''
2044. Count Number of Maximum Bitwise-OR Subsets

2021.10.17 Sunday 15:26
'''
from typing import List
import collections
import copy


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = collections.Counter([0])
        for a in nums:
            _dp = copy.deepcopy(dp)
            for k, v in _dp.items():
                dp[k | a] += v
        return dp[max(dp)]


if __name__ == "__main__":
    obj = Solution()
    assert obj.countMaxOrSubsets(nums = [3,1])==2
    assert obj.countMaxOrSubsets(nums = [2,2,2])==7
    assert obj.countMaxOrSubsets(nums = [3,2,1,5])==6