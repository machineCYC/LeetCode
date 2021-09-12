'''
2001. Number of Pairs of Interchangeable Rectangles

2021.09.12 Sunday 18:18
'''
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        for r in rectangles:
            w, h = r
            ratio = w / h

            if str(ratio) not in count:
                count[str(ratio)] = 1
            else:
                count[str(ratio)] += 1

        ans = 0
        for c in count:
            if count[c] < 2:
                ans += 0
            else:
                ans += (count[c] * (count[c] - 1)) // 2
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.interchangeableRectangles(rectangles = [[4,8],[3,6],[10,20],[15,30]]) == 6
    assert obj.interchangeableRectangles(rectangles = [[4,5],[7,8]]) == 0
