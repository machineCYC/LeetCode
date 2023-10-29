'''
2917. Find the K-or of an Array

2023.10.26 Sunday 15:10
'''
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 31
        for i in range(l):
            cnt = 0
            for n in nums:
                if 2 ** (i) & n == 2 ** (i):
                    cnt += 1
            if cnt >= k:
                ans += 2 ** i
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.findKOr(nums = [7,12,9,8,9,15], k = 4) == 9
    assert obj.findKOr(nums = [2,12,1,11,4,5], k = 6) == 0
    assert obj.findKOr(nums = [10,8,5,9,11,6,8], k = 1) == 15
    assert obj.findKOr(nums = [14,7,12,9,8,9,1,15], k = 4) == 13
    assert obj.findKOr(nums = [2], k = 1) == 2
    assert obj.findKOr(nums = [14,28,23,22], k = 2) == 30