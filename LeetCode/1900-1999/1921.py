'''
1921. Eliminate Maximum Number of Monsters

2021.07.04 Sunday 19:04
'''
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        rs = []
        ans = n
        for d, s in zip(dist, speed):
            if d % s:
                r = d // s + 1
            else:
                r = d // s

            rs.append(r)

        rss = sorted(rs)
        for i in range(1, n):
            cur = rss[i] - i
            if cur == 0:
                ans = i
                break
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.eliminateMaximum(dist = [1,3,4], speed = [1,1,1])==3
    assert obj.eliminateMaximum(dist = [1,1,2,3], speed = [1,1,1,1])==1
    assert obj.eliminateMaximum(dist = [3,2,4], speed = [5,3,2])==1
    assert obj.eliminateMaximum(dist = [4,2,3], speed = [2,1,1])==3
