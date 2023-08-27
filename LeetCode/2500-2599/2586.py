from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for idx, word in enumerate(words):
            if idx >= left and idx <= right and word[-1] in vowels and word[0] in vowels:
                cnt += 1
        return cnt


if __name__ == "__main__":
    obj = Solution()
    assert obj.vowelStrings(words = ["are","amy","u"], left = 0, right = 2) == 2
    assert obj.vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4) == 3