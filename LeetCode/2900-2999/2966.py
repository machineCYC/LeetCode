'''
2966. Divide Array Into Arrays With Max Difference

2023.12.17 Sunday 15:06
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(2, n, 3):
            sub = nums[i-2:i+1]
            if sub[-1] - sub[-2] <= k and sub[-2] - sub[-3] <= k and sub[-1] - sub[-3] <= k:
                ans.append(sub)
            else:
                return []
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2) == [[1,1,3],[3,4,5],[7,8,9]]
    assert obj.divideArray(nums = [1,3,3,2,7,3], k = 3) == []
    assert obj.divideArray(nums = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2], k = 2) == []
