'''
3289. The Two Sneaky Numbers of Digitville

2024.09.22 Sunday 10:16
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        return [c for c in counter if counter[c] > 1]


if __name__ == "__main__":
    obj = Solution()
    assert sorted(obj.getSneakyNumbers(nums = [0,1,1,0])) == sorted([0, 1])
    assert sorted(obj.getSneakyNumbers(nums = [0,3,2,1,3,2])) == sorted([2,3])
    assert sorted(obj.getSneakyNumbers(nums = [7,1,5,4,3,4,6,0,9,5,8,2])) == sorted([4,5])

