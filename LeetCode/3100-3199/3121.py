'''
3121. Count the Number of Special Characters II

2024.04.21 Sunday 14:35
'''
from typing import List


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lower_collect = {}
        upper_collect = {}
        for idx, e in enumerate(word):
            if e == e.lower():
                lower_collect[e] = max(lower_collect.get(e, -1), idx)
            else:
                upper_collect[e.lower()] = min(upper_collect.get(e.lower(), n), idx)

        ans = 0
        for k, v in lower_collect.items():
            upper_v = upper_collect.get(k)
            if upper_v and upper_v > v:
                ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfSpecialChars(word = "aaAbcBC") == 3
    assert obj.numberOfSpecialChars(word = "abc") == 0
    assert obj.numberOfSpecialChars(word = "abBCab") == 0