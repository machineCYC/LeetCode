'''
1984. Minimum Difference Between Highest and Lowest of K Scores

2021.08.29 Sunday 13:39
'''
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        diff = 10**5
        for i in range(k-1, n):
            tmpnums = nums[i-k+1:i+1]
            minv = tmpnums[0]
            maxv = tmpnums[-1]
            if maxv - minv < diff:
                diff = maxv - minv
        return diff


if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumDifference(nums = [90], k = 1) == 0
    assert obj.minimumDifference(nums = [9,4,1,7], k = 2) == 2