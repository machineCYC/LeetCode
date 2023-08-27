'''
1913. Maximum Product Difference Between Two Pairs

2021.06.27 Sunday 15:09
'''
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        ans = sort_nums[-1] * sort_nums[-2] - sort_nums[0] * sort_nums[1]
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxProductDifference(nums = [5,6,2,7,4])==34
    assert obj.maxProductDifference(nums = [4,2,5,9,7,4,8])==64
