'''
3295. Report Spam Message

2024.09.22 Sunday 12:49
'''
from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:

        bannedWords_dict = {w:1 for w in bannedWords}

        cnt = 0
        for m in message:
            if bannedWords_dict.get(m, 0):
                cnt += 1
        return (cnt >=2)




if __name__ == "__main__":
    obj = Solution()
    assert obj.reportSpam(message = ["hello","world","leetcode"], bannedWords = ["world","hello"]) == True
    assert obj.reportSpam(message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]) == False