'''
200. Number of Islands

2021.06.20 Sunday 20:03
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and grid[i][j]=="1"):
                return 0

            grid[i][j] = 0
            for nid, njd in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfs(i + nid, j + njd)
            return 1

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += dfs(i, j)
        return res


if __name__ == "__main__":
    obj = Solution()
    assert obj.numIslands(grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]) == 1
    assert obj.numIslands(grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]) == 3