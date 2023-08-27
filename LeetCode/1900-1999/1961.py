'''
1961. Check If String Is a Prefix of Array

2021.08.08 Sunday 14:13
'''
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            n = len(word)
            if s[i:i+n] == word:
                i += n
            else:
                return False

            if i == len(s):
                return True
        return False


if __name__ == "__main__":
    obj = Solution()
    assert obj.isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"]) == True
    assert obj.isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"]) == False
    assert obj.isPrefixString(s = "a", words = ["aa","aaaa","banana"]) == False
    assert obj.isPrefixString(s = "ccccccccc", words = ["c","cc"]) == False
    assert obj.isPrefixString(s = "a", words = ["a","ad","cookie"]) == True
    assert obj.isPrefixString(s = "aaa", words = ["aa","aaa","fjaklfj"]) == False