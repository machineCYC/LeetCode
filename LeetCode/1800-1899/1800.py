'''
1800. Maximum Ascending Subarray Sum

2021.03.21 Sunday 13:51
'''
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        bef_num = 0
        subarray_sum = 0
        max_subarray_sum = 0
        for n in nums:
            if n > bef_num:
                subarray_sum += n
            else:
                max_subarray_sum = max(max_subarray_sum, subarray_sum)
                subarray_sum = n
            bef_num = n

        return max(max_subarray_sum, subarray_sum)


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxAscendingSum(nums = [10,20,30,5,10,50])==65
    assert obj.maxAscendingSum(nums = [10,20,30,40,50])==150
    assert obj.maxAscendingSum(nums = [12,17,15,13,10,11,12])==33
    assert obj.maxAscendingSum(nums = [100,10,1])==100
