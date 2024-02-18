'''
6916. Prime Pairs With Target Sum

2023.07.02 Sunday 14:26
'''
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1: str, str2:str) -> bool:
            n = len(str1)
            if str2[:n] == str1 and str2[-n:] == str1:
                return True
            return False

        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n, 1):
                if isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"]) == 4
    assert obj.countPrefixSuffixPairs(words = ["pa","papa","ma","mama"]) == 2
    assert obj.countPrefixSuffixPairs(words = ["abab","ab"]) == 0
