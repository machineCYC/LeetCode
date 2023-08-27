'''
1903. Largest Odd Number in String

2021.06.20 Sunday 16:25
'''


class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ''
        n = len(num)
        for i in range(n):
            if int(num[n-i-1]) % 2 == 0:
                ans = num[:n-i-1]
            else:
                ans = num[:n-i]
                break
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.largestOddNumber(num = "52") == "5"
    assert obj.largestOddNumber(num = "4206") == ""
    assert obj.largestOddNumber(num = "35427") == "35427"