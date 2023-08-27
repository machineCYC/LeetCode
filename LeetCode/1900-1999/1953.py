'''
1953. Maximum Number of Weeks for Which You Can Work

2021.08.01 Sunday 13:30
'''
from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _sum = sum(milestones)
        _max = max(milestones)
        if 2 * _max <= _sum:
            return _sum
        return 2 * (_sum - _max) + 1


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfWeeks(milestones = [1,2,3]) == 6
    assert obj.numberOfWeeks(milestones = [5,2,1]) == 7
    assert obj.numberOfWeeks(milestones = [9,3,6,8,2,1]) == 29
