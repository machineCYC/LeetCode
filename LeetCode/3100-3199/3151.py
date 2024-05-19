'''
3151. Special Array I

2024.05.19 Sunday 14:22
'''
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        n = len(nums)
        for i in range(1, n, 1):
            pre = nums[i-1]
            cur = nums[i]
            if cur % 2  == pre % 2:
                return False
        return True


if __name__ == "__main__":
    obj = Solution()
    assert obj.isArraySpecial(nums = [1]) == True
    assert obj.isArraySpecial(nums = [2,1,4]) == True
    assert obj.isArraySpecial(nums = [4,3,1,6]) == False
