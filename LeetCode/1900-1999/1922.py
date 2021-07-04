'''
1922. Count Good Numbers

2021.07.44 Sunday 19:45
'''


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        ans = pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.countGoodNumbers(n = 1)==5
    assert obj.countGoodNumbers(n = 4)==400
    assert obj.countGoodNumbers(n = 50)==564908303