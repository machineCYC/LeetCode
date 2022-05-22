'''
2278. Percentage of Letter in String

2022.05.22 Sunday 12:59
'''


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        ret = [1 if ss == letter else 0 for ss in s]
        return int((sum(ret) / len(ret)) * 100)

if __name__ == "__main__":
    obj = Solution()
    assert obj.percentageLetter(s = "foobar", letter = "o") == 33
    assert obj.percentageLetter(s = "jjjj", letter = "k") == 0
