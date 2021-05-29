'''
2020.09.06 Sunday 13:57
'''

from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        last_ss = None
        last_c = None
        contis = []
        for ss, c in zip(s, cost):
            if last_c == None or last_ss == None:
                contis.append(c)
            else:
                if ss == last_ss:
                    contis.append(c)
                else:
                    if len(contis)>1:
                        ans += sum(contis) - max(contis)
                    contis = []
                    contis.append(c)

            last_ss = ss
            last_c = c

        ans += sum(contis) - max(contis)
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.minCost(s = "abaac", cost = [1,2,3,4,5])==3
    assert obj.minCost(s = "abc", cost = [1,2,3])==0
    assert obj.minCost(s = "aabaa", cost = [1,2,3,4,1])==2
    assert obj.minCost(s = "aaabbbabbbb", cost = [3,5,10,7,5,3,5,5,4,8,1])==26
