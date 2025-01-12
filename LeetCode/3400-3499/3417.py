'''
3417. Zigzag Grid Traversal With Skip

2025.01.12 Sunday 15:15
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        is_pick = True
        for idx, row in enumerate(grid):
            if idx % 2 == 0:
                pass
            else:
                row = row[::-1]

            for col in row:
                if is_pick:
                    ans.append(col)
                    is_pick = False
                else:
                    is_pick = True
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.zigzagTraversal(grid = [[1,2],[3,4]]) == [1,4]
    assert obj.zigzagTraversal(grid = [[2,1],[2,1],[2,1]]) == [2, 1, 2]
    assert obj.zigzagTraversal(grid = [[1,2,3],[4,5,6],[7,8,9]]) == [1,3,5,7,9]
