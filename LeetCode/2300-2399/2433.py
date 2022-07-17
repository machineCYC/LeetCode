'''
2343. Query Kth Smallest Trimmed Number

2022.07.17 Sunday 14:16
'''
from typing import List
from collections import defaultdict


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for k, trim in queries:
            tims_nums = [(n[trim*-1:], i) for i, n in enumerate(nums)]
            ans.append(sorted(tims_nums)[k-1][1])
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]])==[2,2,1,0]
    assert obj.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]])==[3,0]
