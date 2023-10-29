'''
2860. Happy Students

2023.09.17 Sunday 23:50
'''
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        ans = 0

        snums = sorted(nums)
        l = len(snums)
        if snums[0] != 0:
            ans += 1

        if snums[-1] < l:
            ans += 1

        counter = {}
        for n in snums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        for s in range(1, l):
            if s not in counter:
                if snums[s-1] < s and snums[s] > s:
                    ans += 1
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.countWays(nums = [1,1]) == 2
    assert obj.countWays(nums = [6,0,3,3,6,7,2,7]) == 3
    assert obj.countWays(nums =  [1,1,0,1]) == 1
