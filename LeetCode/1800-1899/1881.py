'''
1881. Maximum Value after Insertion

2021.05.30 Sunday 15:01
'''


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        t = str(x)
        if n[0] == "-":
            n = n[1:]
            i = 0
            N = len(n)
            while i < N:
                if t < n[i]:
                    return "-" + n[:i] + t + n[i:]
                i += 1
            return "-" + n + t
        else:
            i = 0
            N = len(n)
            while i < N:
                if t > n[i]:
                    return n[:i] + t + n[i:]
                i += 1
            return n + t


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxValue(n = "99", x = 9) == "999"
    assert obj.maxValue(n = "-13", x = 2) == "-123"
    assert obj.maxValue(n = "-5831", x = 4) == "-45831"
    assert obj.maxValue(n = "-132", x = 3) == "-1323"
