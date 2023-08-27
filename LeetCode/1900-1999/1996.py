'''
1996. The Number of Weak Characters in the Game

2021.09.05 Sunday 13:24
'''
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        stack = []
        for a, d in properties:
            while stack and stack[-1][0] < a and stack[-1][1] < d:
                count += 1
                stack.pop()
            stack.append((a, d))
        return count


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfWeakCharacters(properties = [[1,5],[10,4],[4,3]]) == 1
    assert obj.numberOfWeakCharacters(properties = [[5,5],[6,3],[3,6]]) == 0
    assert obj.numberOfWeakCharacters(properties = [[2,2],[3,3]]) == 1
    assert obj.numberOfWeakCharacters(properties = [[1,1],[2,1],[2,2],[1,2]]) == 1
