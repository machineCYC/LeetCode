'''
1672. Richest Customer Wealth

2020.11.29 Sunday 13:17
'''
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = 0
        for c in accounts:
            w = sum(c)
            max_w = max(max_w, w)
        return max_w

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumWealth(accounts = [[1,2,3],[3,2,1]])==6
    assert obj.maximumWealth(accounts = [[1,5],[7,3],[3,5]])==10
    assert obj.maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]])==17