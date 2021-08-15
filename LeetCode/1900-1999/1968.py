'''
1968. Array With Elements Not Equal to Average of Neighbors

2021.08.15 Sunday 14:27
'''
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                ans.append(nums.pop(0))

            if i % 2 == 1:
                ans.append(nums.pop(-1))
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.rearrangeArray(nums = [1,2,3,4,5])==[1,5,2,4,3]
    assert obj.rearrangeArray(nums = [6,2,0,9,7])==[0,9,2,7,6]
    assert obj.rearrangeArray(nums = [1,3,2])==[1,3,2]
