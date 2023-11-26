'''
2947. Count Beautiful Substrings I

2023.11.26 Sunday 14:08
'''
from typing import List


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:

        def is_beautiful(s: str, k: int) -> True:
            n = len(s)
            vowels_cnt = sum([s.count(x) for x in "aeiou"])
            if vowels_cnt == (n - vowels_cnt) and (vowels_cnt * (n - vowels_cnt) % k == 0):
                return True
            return False

        ans = 0
        n = len(s)
        possible_len = [i for i in range(2, n+1, 2) if ((i // 2) ** 2 % k) == 0 ]
        for idx, v in enumerate(s):
            max_len = n - idx
            for l in possible_len:
                if l <= max_len:
                    ans += 1 if is_beautiful(s[idx:idx+l], k) else 0
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.beautifulSubstrings(s = "baeyh", k = 2) == 2
    assert obj.beautifulSubstrings(s = "abba", k = 1) == 3
    assert obj.beautifulSubstrings(s = "bcdf", k = 1) == 0
