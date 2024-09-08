'''
3281. Maximize Score of Numbers in Ranges

2024.09.08 Sunday 15:47
'''
from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        l = 0
        r = start[-1] - start[0] + d + 1

        def isPossible(score: int) -> bool:
            pre = start[0]
            for i in range(1, n):
                current = pre + score
                if current > start[i] + d:
                    return False
                elif current <= start[i]:
                    pre = start[i]
                else:
                    pre = current
            return True
            # pre = start[0]
            # for i in range(1, n):
            #     if start[i] + d - pre < score:
            #         return False
            #     pre = max(start[i], pre + score)
            # return True

        while l < r:
            m = l + (r - l) // 2
            if isPossible(m):
                l = m + 1
            else:
                r = m
        return l - 1


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxPossibleScore(start = [6,0,3], d = 2) == 4
    assert obj.maxPossibleScore(start = [2,6,13,13], d = 5) == 5
