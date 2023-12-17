'''
2965. Find Missing and Repeated Values

2023.12.17 Sunday 14:31
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnts = [0] * (n * n + 1)

        for row in grid:
            for col in row:
                cnts[col] += 1
                if cnts[col] == 2:
                    a = col

        for idx, c in enumerate(cnts):
            if c == 0 and idx != 0:
                b = idx
                break
        return [a, b]


if __name__ == "__main__":
    obj = Solution()
    assert obj.findMissingAndRepeatedValues(grid = [[1,3],[2,2]]) == [2,4]
    assert obj.findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]) == [9,5]
