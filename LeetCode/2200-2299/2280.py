'''
2280. Minimum Lines to Represent a Line Chart

2022.05.22 Sunday 12:43
'''
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices = sorted(stockPrices)
        n = len(stockPrices)
        if n == 1:
            return 0

        cnt = 1
        c_delta_y = stockPrices[1][1] - stockPrices[0][1]
        c_delta_x = stockPrices[1][0] - stockPrices[0][0]
        n = len(stockPrices)
        for i in range(2, n):
            cx, cy = stockPrices[i]
            px, py = stockPrices[i-1]

            delta_y = cy - py
            delta_x = cx - px

            if (delta_x * c_delta_y) != (c_delta_x * delta_y):
                cnt += 1
                c_delta_y = delta_y
                c_delta_x = delta_x
        return cnt

if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumLines(stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]])==3
    assert obj.minimumLines(stockPrices = [[3,4],[1,2],[7,8],[2,3]])==1
