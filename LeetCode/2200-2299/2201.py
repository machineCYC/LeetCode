'''
2201. Count Artifacts That Can Be Extracted

2022.03.13 Sunday 13:03
'''
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        s = set((dx, dy) for dx, dy in dig)

        cnt = 0
        for art in artifacts:
            flag = 0
            xmin, ymin, xmax, ymax = art
            for xx in range(xmin, xmax+1):
                for yy in range(ymin, ymax+1):
                    if (xx, yy) not in s:
                        flag = 1
                        break
            if flag == 0:
                cnt += 1
        return cnt

if __name__ == "__main__":
    obj = Solution()
    assert obj.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]) == 1
    assert obj.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]) == 2
