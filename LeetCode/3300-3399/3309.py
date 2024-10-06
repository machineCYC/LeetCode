'''
3309. Maximum Possible Number by Binary Concatenation

2024.10.06 Sunday 15:07
'''
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        ans = 0
        bnums = [bin(n)[2:] for n in nums]

        case1 = int("".join([bnums[0], bnums[1], bnums[2]]), 2)
        case2 = int("".join([bnums[0], bnums[2], bnums[1]]), 2)
        case3 = int("".join([bnums[2], bnums[1], bnums[0]]), 2)
        case4 = int("".join([bnums[1], bnums[2], bnums[0]]), 2)
        case5 = int("".join([bnums[1], bnums[0], bnums[2]]), 2)
        case6 = int("".join([bnums[2], bnums[0], bnums[1]]), 2)
        ans = max([case1, case2, case3, case4, case5, case6])
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxGoodNumber(nums = [1,2,3]) == 30
    assert obj.maxGoodNumber(nums = [2,8,16]) == 1296
    assert obj.maxGoodNumber(nums = [5,1,78]) == 1742
