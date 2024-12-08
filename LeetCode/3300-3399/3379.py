'''
3379. Transformed Array

2024.12.08 Sunday 13:19
'''
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [None] * n

        for idx, ele in enumerate(nums):
            if ele > 0:
                value = nums[(idx + ele) % n]
            elif ele < 0:
                value = nums[idx - (abs(ele) % n)]
            else:
                value = nums[idx]
            result[idx] = value
        return result


if __name__ == "__main__":
    obj = Solution()
    assert obj.constructTransformedArray(nums = [3,-2,1,1]) == [1,1,1,3]
    assert obj.constructTransformedArray(nums = [-1,4,-1]) == [-1,-1,4]
    assert obj.constructTransformedArray(nums = [-5]) == [-5]