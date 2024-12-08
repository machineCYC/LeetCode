'''
3355. Zero Array Transformation I

2024.11.17 Sunday 23:40
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array for range operations

        # Process each query
        for li, ri in queries:
            diff[li] += 1
            if ri + 1 < n:
                diff[ri + 1] -= 1

        # Apply the difference array to compute the cumulative decrements
        current_decrement = 0
        for i in range(n):
            current_decrement += diff[i]
            nums[i] -= current_decrement
            if nums[i] < 0:
                nums[i] = 0

        # Check if nums is a zero array
        return all(x == 0 for x in nums)


if __name__ == "__main__":
    obj = Solution()
    assert obj.isZeroArray(nums = [1,0,1], queries = [[0,2]]) == True
    assert obj.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]) == False
    assert obj.isZeroArray(nums = [4,6], queries =[[0,0],[0,1],[1,1],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1],[1,1],[0,0],[1,1],[0,1],[0,0],[1,1]]) == True
