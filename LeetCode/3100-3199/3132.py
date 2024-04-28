'''
3132. Find the Integer Added to Array II

2024.04.28 Sunday 16:17
'''
from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        min_n2 = min(nums2)

        n = len(nums1)
        ans = 1000
        for i in range(n):
            for j in range(i+1, n, 1):
                diffs = list(set([n2-n1 for n1, n2 in zip(nums1[:i] + nums1[i+1:j] + nums1[j+1:], nums2)]))
                if len(diffs) == 1:
                    ans = min(ans, diffs[0])
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumAddedInteger(nums1 = [4,20,16,12,8], nums2 = [14,18,10]) == -2
    assert obj.minimumAddedInteger(nums1 = [4,20,16,12,9], nums2 = [14,18,10]) == -2
    assert obj.minimumAddedInteger(nums1 = [3,5,5,3], nums2 = [7,7]) == 2
