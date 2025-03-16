'''
3487. Maximum Unique Subarray Sum After Deletion

2025.03.16 Sunday 14:28
'''
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos_nums = [n for n in nums if n > 0]
        m = len(pos_nums)
        if m == 0:
            return max(nums)

        ans = 0
        for idx in range(m):
            for idy in range(idx+1, m+1):
                sub_array = pos_nums[idx: idy]
                ans = max(ans, sum(set(sub_array)))
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxSum(nums = [1,2,3,4,5]) == 15
    assert obj.maxSum(nums = [1,1,0,1,1]) == 1
    assert obj.maxSum(nums = [1,2,-1,-2,1,0,-1]) == 3
    assert obj.maxSum(nums = [-2,-1]) == -1
    assert obj.maxSum(nums = [4,0,0,13,1]) == 18
    assert obj.maxSum(nums = [-6,12,20,20,-14,10,-12]) == 42
