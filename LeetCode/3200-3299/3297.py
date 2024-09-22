'''
3297. Count Substrings That Can Be Rearranged to Contain a String I

2024.09.22 Sunday 13:55
'''
from collections import Counter, defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        if len1 < len2:
            return 0

        count = Counter(word2)
        window = defaultdict(int)
        ans = 0
        left = 0
        cur = 0
        for right in range(len1):
            right_value = word1[right]
            window[right_value] += 1
            cur += (right_value in count and window[right_value] == count[right_value])
            while cur == len(count):
                ans += len1 - right

                left_value = word1[left]
                window[left_value] -= 1
                cur -= (left_value in count and window[left_value] == count[left_value] -1)
                left += 1
        return ans



if __name__ == "__main__":
    obj = Solution()
    assert obj.validSubstringCount(word1 = "bcca", word2 = "abc") == 1
    assert obj.validSubstringCount(word1 = "abcabc", word2 = "abc") == 10
    assert obj.validSubstringCount(word1 = "abcabc", word2 = "aaabc") == 0