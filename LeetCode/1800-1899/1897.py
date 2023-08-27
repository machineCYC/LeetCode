'''
1897. Redistribute Characters to Make All Strings Equal

2021.06.13 Sunday 15:23
'''
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        joinword = "".join(words)
        count = {}
        for i in joinword:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for a in set(joinword):
            if count[a] % n != 0:
                return False
        return True

if __name__ == "__main__":
    obj = Solution()
    assert obj.makeEqual(words = ["abc","aabc","bc"]) == True
    assert obj.makeEqual(words = ["ab","a"]) == False
