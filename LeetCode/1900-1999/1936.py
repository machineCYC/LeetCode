'''
1936. Add Minimum Number of Rungs

2021.07.18 Sunday 15:13
'''
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        count = 0
        rungss = [0] + rungs
        n = len(rungss)
        for i in range(1, n):
            curdist = rungss[i] - rungss[i-1]
            if curdist > dist:
                a = curdist // dist
                b = curdist % dist
                add = a - 1 if b == 0 else a
                count += add
        return count

if __name__ == "__main__":
    obj = Solution()
    assert obj.addRungs(rungs = [1,3,5,10], dist = 2) == 2
    assert obj.addRungs(rungs = [3,6,8,10], dist = 3) == 0
    assert obj.addRungs(rungs = [3,4,6,7], dist = 2) == 1
    assert obj.addRungs(rungs = [5], dist = 10) == 0
    assert obj.addRungs(rungs = [3], dist = 1) == 2
    assert obj.addRungs(rungs = [12,24], dist = 4) == 4