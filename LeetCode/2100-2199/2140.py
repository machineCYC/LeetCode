'''
2140. Solving Questions With Brainpower

2022.01.16 Sunday 14:09
'''
from typing import List
# from functools import cache python 3.10


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # @cache
        def dp(i):
            if i >= len(questions):
                return 0
            points, jump = questions[i]
            return max(dp(i+1), points + dp(i+jump+1))
        return dp(0)


if __name__ == "__main__":
    obj = Solution()
    assert obj.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]])==5
    assert obj.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]])==7
