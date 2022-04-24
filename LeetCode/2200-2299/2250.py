'''
2250. Count Number of Rectangles Containing Each Point

2022.04.24 Sunday 16:28
'''
import bisect
from collections import defaultdict
from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        cnt = [0] * len(points)
        rectangles.sort()
        length = defaultdict(list)
        for rectangle in rectangles:
            x, y = rectangle
            length[y].append(x)

        idx = 0
        for point in points:
            px, py = point
            for h in range(py, 101):
                cnt[idx] += len(length[h]) - bisect.bisect_left(length[h], px)
            idx += 1
        return cnt

if __name__ == "__main__":
    obj = Solution()
    assert obj.countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]) == [2, 1]
    assert obj.countRectangles(rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]) == [1, 3]
    assert obj.countRectangles(rectangles = [[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]], points = [[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]]) == [1,0,4,1,0,0,0,1]
