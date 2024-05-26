'''
3164. Find the Number of Good Pairs II

2024.05.26 Sunday 15:47
'''
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2_cnt = {}
        for n2 in nums2:
            value = n2 * k
            if value in nums2_cnt:
                nums2_cnt[value] += 1
            else:
                nums2_cnt[value] = 1

        counts = [0] * (max(nums1) + 1)
        ans = 0
        for k, v in nums2_cnt.items():
            for mul in range(k, len(counts), k):
                counts[mul] += v
        return sum([counts[n1] for n1 in nums1])


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1) == 5
    assert obj.numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3) == 2
    assert obj.numberOfPairs(nums1 = [9], nums2 = [10], k = 9) == 0
