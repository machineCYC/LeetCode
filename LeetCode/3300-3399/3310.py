'''
3310. Remove Methods From Project

2024.10.06 Sunday 16:57
'''
from typing import List
from collections import defaultdict


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        using = defaultdict(list)
        for invocation in invocations:
            a, b = invocation
            if a not in using:
                using[a] = [b]
            else:
                using[a].append(b)

        visited = set()
        check = [k]
        while check:
            cur = check.pop()
            if cur not in visited:
                visited.add(cur)
                for path in using[cur]:
                    if path not in visited:
                        check.append(path)

        for invocation in invocations:
            if invocation[0] not in visited and invocation[1] in visited:
                return [i for i in range(n)]

        return [x for x in range(n) if x not in visited]

if __name__ == "__main__":
    obj = Solution()
    assert sorted(obj.remainingMethods(n = 3, k = 2, invocations = [[1,0],[2,0]])) == [0,1,2]
    assert sorted(obj.remainingMethods(n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]])) == [0,1,2,3]
    assert sorted(obj.remainingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]])) == [3,4]
    assert sorted(obj.remainingMethods(n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]])) == []