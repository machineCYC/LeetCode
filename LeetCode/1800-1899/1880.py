'''
1880. Check if Word Equals Summation of Two Words

2021.05.30 Sunday 14:51
'''


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def transform_w2n(word):
            n = ''
            for w in word:
                n += str(ord(w) - 97)
            return int(n)
        return transform_w2n(firstWord) + transform_w2n(secondWord) == transform_w2n(targetWord)


if __name__ == "__main__":
    obj = Solution()
    assert obj.isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb") == True
    assert obj.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab") == False
    assert obj.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa") == True
