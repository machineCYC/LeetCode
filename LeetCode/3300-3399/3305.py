'''
3305. Count of Substrings Containing Every Vowel and K Consonants I

2024.09.29 Sunday 12:24
'''


class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        for i in range(n):
            cnt_a = 0
            cnt_e = 0
            cnt_i = 0
            cnt_o = 0
            cnt_u = 0
            cnt_other = 0
            for j in range(i, n, 1):
                if word[j] == "a":
                    cnt_a += 1
                elif word[j] == "e":
                    cnt_e += 1
                elif word[j] == "i":
                    cnt_i += 1
                elif word[j] == "o":
                    cnt_o += 1
                elif word[j] == "u":
                    cnt_u += 1
                else:
                    cnt_other += 1

                if cnt_a > 0 and cnt_e > 0 and cnt_i > 0 and cnt_o > 0 and cnt_u > 0 and cnt_other == k:
                    ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countOfSubstrings(word = "aeioqq", k = 1) == 0
    assert obj.countOfSubstrings(word = "aeiou", k = 0) == 1
    assert obj.countOfSubstrings(word = "ieaouqqieaouqq", k = 1) == 3
    assert obj.countOfSubstrings(word = "iaaaeaouqqieaouqq", k = 1) == 3
    assert obj.countOfSubstrings(word = "k", k = 1) == 0
    assert obj.countOfSubstrings(word = "iqeaouqi", k = 2) == 3
