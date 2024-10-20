'''
3324. Find the Sequence of Strings Appeared on the Screen

2024.10.20 Sunday 14:49
'''
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []

        prefix = ""
        for t in target:
            order = ord(t)
            tmp = [prefix + chr(idx+97) for idx in range(order-96)]
            ans.extend(tmp)
            prefix = tmp[-1]
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.stringSequence(target = "abc") == ["a","aa","ab","aba","abb","abc"]
    assert obj.stringSequence(target = "he") == ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
