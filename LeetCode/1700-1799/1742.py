'''
1742. Maximum Number of Balls in a Box

2021.01.31 Sunday 17:26
'''
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum_digits(number):
            r = 0
            while number:
                r += number % 10
                number //= 10
            return r

        n = highLimit - lowLimit + 1
        ret = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            ret[sum_digits(i)] += 1

        return max([ret[k] for k in ret])

if __name__ == "__main__":
    obj = Solution()
    assert obj.countBalls(lowLimit = 1, highLimit = 10)==2
    assert obj.countBalls(lowLimit = 5, highLimit = 15)==2
    assert obj.countBalls(lowLimit = 19, highLimit = 28)==2