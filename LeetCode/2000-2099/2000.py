'''
2000. Reverse Prefix of Word

2021.09.12 Sunday 18:04
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        isfirst = True
        ans = []
        for w in word:
            if w == ch and isfirst:
                ans = [w] + ans[::-1]
                isfirst = False
            else:
                ans.append(w)
        return "".join(ans)

if __name__ == "__main__":
    obj = Solution()
    assert obj.reversePrefix(word = "abcdefd", ch = "d")=="dcbaefd"
    assert obj.reversePrefix(word = "xyxzxe", ch = "z")=="zxyxxe"
    assert obj.reversePrefix(word = "abcd", ch = "z")=="abcd"
