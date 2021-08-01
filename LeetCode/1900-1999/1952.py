'''
1952. Three Divisors

2021.08.01 Sunday 13:32
'''


class Solution:
    def isThree(self, n: int) -> bool:
        c = 0
        for i in range(1, n+1):
            if n % i == 0:
                c += 1
                if c > 3:
                    return False
        return c == 3


if __name__ == "__main__":
    obj = Solution()
    assert obj.isThree(n = 2) == False
    assert obj.isThree(n = 4) == True
