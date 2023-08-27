'''
2828. Check if a String Is an Acronym of Words

2023.08.20 Sunday 15:10
'''
from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        sw = [w[0] for w in words]
        return "".join(sw) == s


if __name__ == "__main__":
    obj = Solution()
    assert obj.isAcronym(words = ["alice","bob","charlie"], s = "abc") == True
    assert obj.isAcronym(words = ["never","gonna","give","up","on","you"], s = "ngguoy") == True
    assert obj.isAcronym(words = ["an","apple"], s = "a") == False
