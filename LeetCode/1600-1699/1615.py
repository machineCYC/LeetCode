'''
1615. Maximal Network Rank

2020.10.11 Sunday 14:02
'''
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ret = {i:set() for i in range(n)}
        for i, r in enumerate(roads):
            c1, c2 = r
            ret[c1].add(i)
            ret[c2].add(i)

        max_size = 0
        for i in range(n):
            for j in range(i+1, n):
                size = len(ret[i].union(ret[j]))
                max_size = max(max_size, size)
        return max_size


if __name__ == "__main__":
    obj = Solution()
    assert obj.maximalNetworkRank(n = 4,roads = [[0,1],[0,3],[1,2],[1,3]])==4
    assert obj.maximalNetworkRank(n = 5,roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])==5
    assert obj.maximalNetworkRank(n = 8,roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])==5
