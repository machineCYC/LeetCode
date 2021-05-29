'''
1754. Largest Merge Of Two Strings

2021.02.07 Sunday 14:44
'''


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        n_word1 = word1
        n_word2 = word2
        while (n_word1 and n_word2):
            if n_word1 > n_word2:
                merge += n_word1[0]
                n_word1 = n_word1[1:]
            else:
                merge += n_word2[0]
                n_word2 = n_word2[1:]

        merge += n_word1
        merge += n_word2

        return merge

if __name__ == "__main__":
    obj = Solution()
    assert obj.largestMerge(word1 = "cabaa", word2 = "bcaaa")=="cbcabaaaaa"
    assert obj.largestMerge(word1 = "abcabc", word2 = "abdcaba")=="abdcabcabcaba"
    assert obj.largestMerge(word1 = "ddwdddddddddddddwwddddddwddw", word2 = "wwwwwwwwwddwwdwwwwwwwwwwwwwww")=="wwwwwwwwwddwwdwwwwwwwwwwwwwwwddwdddddddddddddwwddddddwddw"

