'''
1935. Maximum Number of Words You Can Type

2021.07.18 Sunday 15:10
'''


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words_list = text.split(" ")
        n = len(words_list)
        for w in text.split(" "):
            for l in list(brokenLetters):
                if l in w:
                    n -= 1
                    break
        return n


if __name__ == "__main__":
    obj = Solution()
    assert obj.canBeTypedWords(text = "hello world", brokenLetters = "ad") == 1
    assert obj.canBeTypedWords(text = "leet code", brokenLetters = "lt") == 1
    assert obj.canBeTypedWords(text = "leet code", brokenLetters = "e") == 0
