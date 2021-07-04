'''
1920. Build Array from Permutation

2021.07.04 Sunday 19:33
'''
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(n)]
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.buildArray(nums = [0,2,1,5,3,4])==[0,1,2,4,5,3]
    assert obj.buildArray(nums = [5,0,1,2,3,4])==[4,5,0,1,2,3]
