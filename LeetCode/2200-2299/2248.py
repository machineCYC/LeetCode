'''
2248. Intersection of Multiple Arrays

2022.04.24 Sunday 16:13
'''
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        def intersection(num1, num2):
            return [i for i in num1 if i in num2]

        for idx, num in enumerate(nums):
            if idx == 0:
                cur = num
            else:
                cur = intersection(cur, num)
        return sorted(cur)


if __name__ == "__main__":
    obj = Solution()
    assert obj.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3,4]
    assert obj.intersection(nums = [[1,2,3],[4,5,6]]) == []
