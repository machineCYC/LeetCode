'''
1614. Maximum Nesting Depth of the Parentheses

2020.10.11 Sunday 13:19
'''


class Solution:
    def maxDepth(self, s: str) -> int:
        curr_max = 0
        final_max = 0
        for ss in s:
            if ss == "(":
                curr_max += 1

                if curr_max > final_max:
                    final_max = curr_max
            elif ss == ")":
                if curr_max > 0:
                    curr_max -= 1

        return final_max

if __name__ == "__main__":
    obj = Solution()
    assert obj.maxDepth(s = "(1+(2*3)+((8)/4))+1")==3
    assert obj.maxDepth(s = "(1)+((2))+(((3)))")==3
    assert obj.maxDepth(s = "1+(2*3)/(2-1)")==1
    assert obj.maxDepth(s = "1")==0
