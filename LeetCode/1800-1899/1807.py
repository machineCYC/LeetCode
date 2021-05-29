'''
1807. Evaluate the Bracket Pairs of a String

2021.03.28 Sunday 13:46
'''
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {i[0]:i[1] for i in knowledge}
        keys = []
        k = ""
        isadd = False
        for ss in s:
            if ss == "(":
                isadd = True
            elif ss == ")":
                keys.append(knowledge_dict.get(k, "?"))
                k = ""
                isadd = False
            elif isadd:
                k += ss
            else:
                keys.append(ss)
        return "".join(keys)


if __name__ == "__main__":
    obj = Solution()
    assert obj.evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]])=="bobistwoyearsold"
    assert obj.evaluate(s = "hi(name)", knowledge = [["a","b"]])=="hi?"
    assert obj.evaluate(s = "(a)(a)(a)aaa", knowledge = [["a","yes"]])=="yesyesyesaaa"
    assert obj.evaluate(s = "(a)(b)", knowledge = [["a","b"],["b","a"]])=="ba"