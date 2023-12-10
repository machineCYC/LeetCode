'''
2961. Double Modular Exponentiation

2023.12.10 Sunday 14:15
'''
from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for idx, v in enumerate(variables):
            if (v[0] ** v[1] % 10) ** v[2] % v[3] == target:
                ans.append(idx)
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2) == [0, 2]
    assert obj.getGoodIndices(variables = [[39,3,1000,1000]], target = 17) == []
