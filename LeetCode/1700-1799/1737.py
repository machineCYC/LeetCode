'''
1737. Change Minimum Characters to Satisfy One of Three Conditions

2021.01.24 Sunday 19:00
'''
from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m = len(a)
        n = len(b)

        c1 = Counter([ord(i)-97 for i in a])
        c2 = Counter([ord(i)-97 for i in b])
        ret = m + n - max((c1+c2).values()) # condiction3
        for i in range(26):
            c1[i+1] += c1[i]
            c2[i+1] += c2[i]

            ret = min(ret, m - c1[i] + c2[i]) # condiction1
            ret = min(ret, n + c1[i] - c2[i]) # condiction2
        return ret


if __name__ == "__main__":
    obj = Solution()
    assert obj.minCharacters(a = "aba", b = "caa")==2
    assert obj.minCharacters(a = "dabadd", b = "cda")==3
    assert obj.minCharacters(a = "bd", b = "a")==0
    assert obj.minCharacters(a = "a", b="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")==2
