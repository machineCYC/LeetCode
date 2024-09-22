'''
3290. Maximum Multiplication Score

2024.09.22 Sunday 15:43
'''
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # dp[i1][i2] represents the maximum score using the first i1 elements from a and first i2 elements from b
        n = len(b)
        dp = [[-1e-11]*n for _ in range(4)]

        dp[0][0] = a[0] * b[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], a[0] * b[i])

        dp[1][1] = dp[0][0] + a[1] * b[1]
        for i in range(2, n):
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + a[1] * b[i])

        dp[2][2] = dp[1][1] + a[2] * b[2]
        for i in range(3, n):
            dp[2][i] = max(dp[2][i-1], dp[1][i-1] + a[2] * b[i])

        dp[3][3] = dp[2][2] + a[3] * b[3]
        for i in range(4, n):
            dp[3][i] = max(dp[3][i-1], dp[2][i-1] + a[3] * b[i])

        return dp[3][n-1]

if __name__ == "__main__":
    obj = Solution()
    assert obj.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]) == 26
    assert obj.maxScore(a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]) == -1
    assert obj.maxScore(a = [100000,100000,100000,100000], b =[-100000,-100000,-100000,-100000]) == -40000000000


