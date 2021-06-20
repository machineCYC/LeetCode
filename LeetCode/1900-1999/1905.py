'''
1905. Count Sub Islands

2021.06.20 Sunday 20:23
'''
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and grid2[i][j] == 1):
                return 1

            grid2[i][j] = 0
            res = grid1[i][j]
            for nid, njd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res &= dfs(i + nid, j + njd)
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    ans += dfs(i, j)

        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])==3
    assert obj.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]])==2