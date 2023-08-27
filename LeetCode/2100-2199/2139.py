'''
2139. Minimum Moves to Reach Target Score

2022.01.16 Sunday 13:25
'''
from typing import List


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1 and maxDoubles > 0:
            ans += 1 + target % 2
            maxDoubles -= 1
            target >>= 1
        return ans + target-1


if __name__ == "__main__":
    obj = Solution()
    assert obj.minMoves(target = 5, maxDoubles = 0)==4
    assert obj.minMoves(target = 19, maxDoubles = 2)==7
    assert obj.minMoves(target = 10, maxDoubles = 4)==4
    assert obj.minMoves(target = 656101987, maxDoubles = 1)==328050994