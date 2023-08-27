'''
1937. Maximum Number of Points with Cost

2021.07.18 Sunday 18:07
'''
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        if m == 1: return max(points[0])
        if n == 1: return sum(sum(x) for x in points)

        def left(pre):
            lft = [pre[0]] + [0] * (n-1)
            for i in range(1, n):
                lft[i] = max(pre[i], lft[i-1]-1)
            return lft


        def right(pre):
            rgt = [0] * (n-1) + [pre[-1]]
            for i in range(n-2, -1, -1):
                rgt[i] = max(pre[i], rgt[i+1]-1)
            return rgt

        pre = points[0]
        for i in range(m - 1):
            cur = [0] * n
            lft = left(pre)
            rgt = right(pre)
            for j in range(n):
                cur[j] = points[i+1][j] + max(lft[j], rgt[j])
            pre = cur
        return max(cur)


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxPoints(points = [[1,2,3],[1,5,1],[3,1,1]]) == 9
    assert obj.maxPoints(points = [[1,5],[2,3],[4,2]]) == 11