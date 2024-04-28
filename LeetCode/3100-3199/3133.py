'''
3133. Minimum Array End

2024.04.28 Sunday 14:22
'''
from typing import List


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # ans = x
        # for i in range(n-1):
        #     ans = (ans + 1) | x
        # return ans

        n -= 1
        i = 0
        while n:
            while x & 1<<i: # avoid do action in the value l i position(right to left)
                i += 1
            if n & 1:
                x ^= 1 << i

            n >>= 1
            i += 1
        return x



if __name__ == "__main__":
    obj = Solution()
    assert obj.minEnd(n = 4, x = 4) == 7
    assert obj.minEnd(n = 3, x = 4) == 6
    assert obj.minEnd(n = 2, x = 7) == 15
