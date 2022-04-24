'''
2249. Count Lattice Points Inside a Circle

2022.04.24 Sunday 16:20
'''
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for circle in circles:
            x, y, r = circle
            left_down_pont = (x-r, y-r)
            l = 2 * r
            for xx in range(left_down_pont[0], left_down_pont[0] + l + 1):
                for yy in range(left_down_pont[1], left_down_pont[1] + l + 1):
                    if ((xx - x) ** 2 + (yy - y) ** 2) ** 0.5 <= r:
                        res.add((xx, yy))
        return len(res)

if __name__ == "__main__":
    obj = Solution()
    assert obj.countLatticePoints(circles = [[2,2,1]]) == 5
    assert obj.countLatticePoints(circles = [[2,2,2],[3,4,1]]) == 16
