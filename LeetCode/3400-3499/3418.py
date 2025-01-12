'''
3418. Maximum Amount of Money Robot Can Earn

2025.01.12 Sunday 15:17
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == j == 0:
                        max_without_neutral = 0
                    else:
                        max_profit_from_top = dp[i-1][j][k] if i > 0 else float('-inf')
                        max_profit_from_left = dp[i][j-1][k] if j > 0 else float('-inf')
                        max_without_neutral = max(max_profit_from_top, max_profit_from_left)

                    # Update DP value without neutralizing
                    dp[i][j][k] = max_without_neutral + coins[i][j]

                    # If the current cell is a robber and we can neutralize it
                    if coins[i][j] < 0 and k > 0:
                        if i == j == 0:
                            max_profit_with_neutral = 0
                        else:
                            max_profit_with_neutral = max(
                                dp[i-1][j][k-1] if i > 0 else float('-inf'),
                                dp[i][j-1][k-1] if j > 0 else float('-inf')
                            )
                        dp[i][j][k] = max(dp[i][j][k], max_profit_with_neutral)
        return max(dp[m-1][n-1])

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumAmount(coins = [[0,1,-1],[1,-2,3],[2,-3,4]]) == 8
    assert obj.maximumAmount(coins = [[10,10,10],[10,10,10]]) == 40
    assert obj.maximumAmount(coins =[[-4]]) == 0
    assert obj.maximumAmount(coins=[[5]]) == 5
    assert obj.maximumAmount(coins = [[-1,1,-1],[1,-2,3],[2,-3,4]]) == 8