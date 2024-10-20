'''
3325. Count Substrings With K-Frequency Characters I

2024.10.20 Sunday 15:50
'''
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        match_flag = False
        counter = defaultdict(int)
        for i in range(n):
            for j in range(i, n):
                counter[s[j]] += 1
                if counter[s[j]] >= k:
                    match_flag = True

                if match_flag:
                    ans += 1
            counter = defaultdict(int)
            match_flag = False
        return ans



if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfSubstrings(s = "abacb", k = 2) == 4
    assert obj.numberOfSubstrings(s = "abcde", k = 1) == 15
