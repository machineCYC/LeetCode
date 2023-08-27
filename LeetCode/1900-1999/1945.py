'''
1945. Sum of Digits of String After Convert

2021.07.25 Sunday 14:42
'''


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convert2nbr(s):
            ans = ''
            for ss in s:
                nbr = ord(ss) - 96
                ans += str(nbr)
            return ans

        def sumdigits(str_nbr):
            ret = 0
            for i in list(str_nbr):
                ret += int(i)
            return ret

        str_nbr = convert2nbr(s)
        ans = 0
        for i in range(k):
            nbr = sumdigits(str_nbr)
            str_nbr = str(nbr)
        return int(str_nbr)


if __name__ == "__main__":
    obj = Solution()
    assert obj.getLucky(s = "iiii", k = 1)==36
    assert obj.getLucky(s = "leetcode", k = 2)==6
    assert obj.getLucky(s = "zbax", k = 2)==8
