'''
2951. Find the Peaks

2023.12.03 Sunday 13:50
'''
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        n = len(mountain)
        for i in range(0, n-2, 1):
            windows = mountain[i:i+3]
            if windows[1] > windows[0] and windows[1] > windows[2]:
                ans.append(i+1)
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.findPeaks(mountain = [2,4,4]) == []
    assert obj.findPeaks(mountain = [1,4,3,8,5]) == [1,3]
