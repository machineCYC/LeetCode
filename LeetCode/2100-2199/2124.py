'''
2124. Check if All A's Appears Before All B's

2022.01.02 Sunday 17:18
'''


class Solution:
    def checkString(self, s: str) -> bool:
        is_b = False
        for ss in s:
            if ss == "b":
                is_b = True

            if is_b and ss == "a":
                return False
        return True

if __name__ == "__main__":
    obj = Solution()
    assert obj.checkString(s = "aaabbb") == True
    assert obj.checkString(s = "abab") == False
    assert obj.checkString(s = "bbb") == True