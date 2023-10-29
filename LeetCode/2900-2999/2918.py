'''
2918. Minimum Equal Sum of Two Arrays After Replacing Zeros

2023.10.29 Sunday 15:10
'''
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(max(n, 1) for n in nums1)
        s2 = sum(max(n, 1) for n in nums2)
        if s1 > s2 and nums2.count(0) == 0:
            return -1

        if s2 > s1 and nums1.count(0) == 0:
            return -1

        return max(s1, s2)


if __name__ == "__main__":
    obj = Solution()
    assert obj.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]) == 12
    assert obj.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0,0]) == 13
    assert obj.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0,0,0]) == 14
    assert obj.minSum(nums1 = [3,2,0,1,0,0,0,0,0,0], nums2 = [6,5,0]) == 13
    assert obj.minSum(nums1 = [2,0,2,0], nums2 = [1,4]) == -1
    assert obj.minSum(nums1 = [9,5], nums2 = [15,12,5,21,4,26,27,9,6,29,0,18,16,0,0,0,20]) == -1
