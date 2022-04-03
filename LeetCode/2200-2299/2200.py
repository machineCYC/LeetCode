'''
2200. Find All K-Distant Indices in an Array

2022.03.13 Sunday 13:07
'''
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = len(nums)
        ans = []
        for idx, n in enumerate(nums):
            if n == key:
                st = max(idx-k, 0)
                ed = min(idx+k+1, l)
                ans.extend([i for i in range(st, ed)])
        return sorted(list(set(ans)))

if __name__ == "__main__":
    obj = Solution()
    assert obj.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)==[1,2,3,4,5,6]
    assert obj.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2)==[0, 1,2,3,4]