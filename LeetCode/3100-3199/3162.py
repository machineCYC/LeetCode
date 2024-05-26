'''
3162. Find the Number of Good Pairs I

2024.05.24 Sunday 15:20
'''
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for n1 in nums1:
            for n2 in nums2:
                if n1 % (n2 * k) == 0:
                    ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1) == 5
    assert obj.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3) == 2
