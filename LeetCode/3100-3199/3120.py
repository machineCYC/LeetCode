'''
3120. Count the Number of Special Characters I

2024.04.21 Sunday 14:22
'''
from typing import List


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_collect = set()
        upper_collect = set()
        for e in word:
            if e == e.lower():
                lower_collect.add(e)
            else:
                upper_collect.add(e.lower())

        return len(lower_collect.intersection(upper_collect))


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfSpecialChars(word = "aaAbcBC") == 3
    assert obj.numberOfSpecialChars(word = "abc") == 0
    assert obj.numberOfSpecialChars(word = "abBCab") == 1