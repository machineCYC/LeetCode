'''
2303. Calculate Amount Paid in Taxes

2022.06.12 Sunday 13:31
'''
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        ans = prev = 0
        for dollors, rate in brackets:
            dollors = min(dollors, income)
            ans += (dollors - prev) * rate / 100
            prev = dollors
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.calculateTax(brackets = [[3,50],[7,10],[12,25]], income = 10) == 2.65
    assert obj.calculateTax(brackets = [[1,0],[4,25],[5,50]], income = 2) == 0.25
    assert obj.calculateTax(brackets = [[2,50]], income = 0) == 0
