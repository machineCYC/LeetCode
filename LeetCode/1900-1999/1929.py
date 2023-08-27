'''
1929. Concatenation of Array

2021.07.11 Sunday 14:44
'''
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "___main__":
    obj = Solution()
    assert obj.getConcatenation(nums = [1,2,1]) == [1,2,1,1,2,1]
    assert obj.getConcatenation(nums = [1,3,2,1]) == [1,3,2,1,1,3,2,1]
