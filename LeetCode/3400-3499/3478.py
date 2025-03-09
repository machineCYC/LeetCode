'''
3478. Choose K Elements With Maximum Sum

2025.03.09 Sunday 20:14
'''
from typing import List
import heapq


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        sindex = sorted(range(n), key = lambda x: (nums1[x], nums2[x]))

        values = {}
        _heap = []
        total_topk_sum = 0
        for sidx in sindex:
            prev = total_topk_sum
            total_topk_sum += nums2[sidx]
            heapq.heappush(_heap, nums2[sidx])
            if len(_heap) > k:
                total_topk_sum -= heapq.heappop(_heap)
            if nums1[sidx] not in values:
                values[nums1[sidx]] = prev
        return [values[ele] for ele in nums1]


if __name__ == "__main__":
    obj = Solution()
    assert obj.findMaxSum(nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2) == [80,30,0,80,50]
    assert obj.findMaxSum(nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1) == [0,0,0,0]
    assert obj.findMaxSum(nums1 = [18,11,24,9,10,11,7,29,16], nums2 = [28,26,27,4,2,19,23,1,2], k = 1) == [26,23,28,23,23,23,0,28,26]
    assert obj.findMaxSum(nums1 =[25,15,1,28,3,13,29,26,1,2,28,5,2,14,19,2,4], nums2 =[25,21,3,23,26,6,30,22,27,21,24,27,15,17,15,16,25], k = 9) == [195,180,0,211,82,160,220,205,0,30,211,133,30,166,195,30,108]
