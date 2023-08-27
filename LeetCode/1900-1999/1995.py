'''
1995. Count Special Quadruplets

2021.09.05 Sunday 13:08
'''
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            count += 1
        return count

if __name__ == "__main__":
    obj = Solution()
    assert obj.countQuadruplets(nums = [1,2,3,6])==1
    assert obj.countQuadruplets(nums = [3,3,6,4,5])==0
    assert obj.countQuadruplets(nums = [1,1,1,3,5])==4
    assert obj.countQuadruplets(nums = [28,8,49,85,37,90,20,8])==1