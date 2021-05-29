'''
1631. Path With Minimum Effort

2020.10.25 Sunday 14:33
'''
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r = len(heights)
        c = len(heights[0])
        heap = [(0, 0, 0)]
        res = 0
        visited = set()
        while heap:
            # Always pop up the smaller abs distance
            d, x, y = heapq.heappop(heap)

            res = max(res, d)
            if x==r-1 and y==c-1:
                return res

            visited.add((x, y))
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (nx>=0 and nx<r) and (ny>=0 and ny<c) and ((nx, ny) not in visited):
                    dn = abs(heights[x][y] - heights[nx][ny])
                    heapq.heappush(heap, (dn, nx, ny))

        return res


if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]])==2
    assert obj.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]])==1
    assert obj.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])==0
