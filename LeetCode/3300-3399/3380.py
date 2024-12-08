'''
3380. Maximum Area Rectangle With Point Constraints I

2024.12.08 Sunday 13:28
'''
from typing import List


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        max_area = -1
        point_set = set(map(tuple, points))
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1  = points[i]
                x2, y2 = points[j]

                if x1 != x2 and y1 != y2:
                    if (x2, y1) in point_set and (x1, y2) in point_set:
                        x_min, x_max = min(x1, x2), max(x1, x2)
                        y_min, y_max = min(y1, y2), max(y1, y2)
                        valid = True

                        for px, py in points:
                            if ((x_min < px < x_max) and (y_min < py < y_max)) or ((px == x_min or px == x_max) and (y_min < py < y_max)) or ((py == y_min or py == y_max) and (x_min < px < x_max)):
                                valid = False
                                break

                        if valid:
                            area = abs(x2 - x1) * abs(y2 - y1)
                            max_area = max(max_area, area)
        return max_area

if __name__ == "__main__":
    obj = Solution()
    assert obj.maxRectangleArea(points = [[1,1],[1,3],[3,1],[3,3]]) == 4
    assert obj.maxRectangleArea(points = [[1,1],[1,3],[3,1],[3,3],[2,2]]) == -1
    assert obj.maxRectangleArea(points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]) == 2
    assert obj.maxRectangleArea(points =[[100,80],[67,79],[100,79],[67,80],[80,47]]) == 33
