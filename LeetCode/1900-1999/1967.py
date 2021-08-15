'''
1967. Number of Strings That Appear as Substrings in Word

2021.08.15 Sunday 14:25
'''
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count

if __name__ == "__main__":
    obj = Solution()
    assert obj.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc")==3
    assert obj.numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb")==2
    assert obj.numOfStrings(patterns = ["a","a","a"], word = "ab")==3
