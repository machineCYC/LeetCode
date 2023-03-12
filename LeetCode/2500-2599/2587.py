from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        cnt = 0
        cumsum = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum > 0:
                cnt += 1
        return cnt


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxScore(nums = [2,-1,0,1,-3,3,-3]) == 6
    assert obj.maxScore(nums = [-2,-3,0]) == 0
