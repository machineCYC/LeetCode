'''
2357. Make Array Zero by Subtracting Equal Amounts

2022.08.01 Monday 19:48
'''
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})

if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumOperations(nums = [1,5,0,3,5])==3
    assert obj.minimumOperations(nums = [0])==0
