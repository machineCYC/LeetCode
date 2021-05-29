'''
1743. Restore the Array From Adjacent Pairs

2021.01.31 Sunday 18:30
'''
from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        indexer = defaultdict(list)
        for n in adjacentPairs:
            l, r = n
            indexer[l].append(r)
            indexer[r].append(l)

        visited = {k:False for k in indexer}
        edges = [k for k in indexer if len(indexer[k])==1]

        res = []
        def dfs(u):
            res.append(u)
            visited[u] = True
            for v in indexer[u]:
                if not visited[v]:
                    dfs(v)

        dfs(edges[0])
        return res

if __name__ == "__main__":
    obj = Solution()
    assert obj.restoreArray(adjacentPairs = [[2,1],[3,4],[3,2]]) == [1,2,3,4]
    assert obj.restoreArray(adjacentPairs = [[4,-2],[1,4],[-3,1]]) == [-2,4,1,-3]
    assert obj.restoreArray(adjacentPairs = [[100000,-100000]]) == [100000,-100000]