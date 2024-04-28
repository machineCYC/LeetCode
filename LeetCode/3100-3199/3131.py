'''
Find the Integer Added to Array I

2024.04.28 Sunday 16:16
'''
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        for n1, n2 in zip(sorted(nums1), sorted(nums2)):
            return n2 - n1



if __name__ == "__main__":
    obj = Solution()
    assert obj.addedInteger(nums1 = [2,6,4], nums2 = [9,7,5]) == 3
    assert obj.addedInteger(nums1 = [10], nums2 = [5]) == -5
    assert obj.addedInteger(nums1 = [1,1,1,1], nums2 = [1,1,1,1]) == 0