'''
2894. Divisible and Non-divisible Sums Difference

2023.10.02 Sunday 12:21
'''


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0
        for i in range(1, n+1, 1):
            if i % m == 0:
                ans -= i
            else:
                ans += i
        return ans


if __name__ == "__main__":
    obj = Solution()
    obj.differenceOfSums(n = 10, m = 3) == 19
    obj.differenceOfSums(n = 5, m = 6) == 15
    obj.differenceOfSums(n = 5, m = 1) == -15
