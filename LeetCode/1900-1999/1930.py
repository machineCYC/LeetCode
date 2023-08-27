'''
1930. Unique Length-3 Palindromic Subsequences

2021.07.11 Sunday 14:46
'''


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        n = len(s)
        for ss in set(s):
            findex = s.index(ss)
            lindex = n - 1 - s[::-1].index(ss)

            if findex != lindex:
                for sss in s[findex+1:lindex]:
                    ans.add(s[findex] + sss + s[lindex])
        return len(ans)


if __name__ == "__main__":
    obj = Solution()
    assert obj.countPalindromicSubsequence(s = "aabca")==3
    assert obj.countPalindromicSubsequence(s = "adc")==0
    assert obj.countPalindromicSubsequence(s = "bbcbaba")==4
