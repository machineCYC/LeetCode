'''
1785. Minimum Elements to Add to Form a Given Sum

2021.03.07 Sunday 13:42
'''
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        abs_diff = abs(goal - total)
        rem = abs_diff % limit
        count = abs_diff // limit

        ans = count + 1 if rem else count
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.minElements(nums = [1,-1,1], limit = 3, goal = -4) == 2
    assert obj.minElements(nums = [1,-10,9,1], limit = 100, goal = 0) == 1
