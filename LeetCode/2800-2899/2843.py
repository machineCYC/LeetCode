'''
2843. Count Symmetric Integers

2023.09.03 Sunday 13:05
'''


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def list_sum(list_str):
            res = 0
            for i in list_str:
                res+=int(i)
            return res
        ans = 0
        for i in range(low, high+1, 1):
            str_digit = str(i)
            n = len(str_digit)
            if n % 2 == 0 and list_sum(list(str_digit[:n//2])) == list_sum(list(str_digit[n//2:])):
                ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countSymmetricIntegers(low = 1, high = 100)==9
    assert obj.countSymmetricIntegers(low = 1200, high = 1230)==4
