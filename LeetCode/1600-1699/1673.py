'''
1673. Find the Most Competitive Subsequence

2020.11.29 Sunday 13:08
'''
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and (len(stack) - 1 + len(nums)-i)>=k:
                    stack.pop()

            if len(stack)<k:
                stack.append(n)
        return stack

if __name__ == "__main__":
    obj = Solution()
    assert obj.mostCompetitive(nums = [3,5,2,6], k=2)==[2,6]
    assert obj.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k=4)==[2,3,3,4]
    assert obj.mostCompetitive(nums = [71,18,52,29,55,73,24,42,66,8,80,2], k=3)==[8, 80, 2]

