'''
2952. Minimum Number of Coins to be Added

2023.12.03 Sunday 13:49
'''
from typing import List
from collections import defaultdict


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        _sum = defaultdict(int)
        for c in coins:
            _sum[c] += c

        ans = 0
        max_value = 0
        for i in range(1, target+1, 1):
            if i in _sum:
                max_value += _sum[i]
            elif i > max_value:
                max_value += i
                ans += 1
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumAddedCoins(coins = [1,4,10], target = 19) == 2
    assert obj.minimumAddedCoins(coins = [1,4,10,5,7,19], target = 19) == 1
    assert obj.minimumAddedCoins(coins = [1,1,1], target = 20) == 3
