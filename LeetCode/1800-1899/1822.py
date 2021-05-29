'''
1822. Sign of the Product of an Array

2021.04.11 Sunday 22:20
'''
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ret = 1
        for n in nums:
            if n == 0:
                return 0

            if n < 0:
                ret = -ret
        return ret


if __name__ == "__main__":
    obj = Solution()
    assert obj.arraySign(nums=[-1,-2,-3,-4,3,2,1])==1
    assert obj.arraySign(nums=[1,5,0,2,-3])==0
    assert obj.arraySign(nums=[-1,1,-1,1,-1])==-1

