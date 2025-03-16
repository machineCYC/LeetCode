'''
3488. Closest Equal Element Queries

2025.03.16 Sunday 14:27
'''
from typing import List
import bisect
from collections import defaultdict


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []

        count_mapping = defaultdict(int)
        indexing_mapp = defaultdict(list)
        n = len(nums)

        for idx, m in enumerate(nums):
           indexing_mapp[m].append(idx)
           count_mapping[m] += 1

        for q in queries:
            if count_mapping[nums[q]] == 1:
                ans.append(-1)
            else:
                indexs = indexing_mapp[nums[q]]
                r_idx = bisect.bisect_right(indexs, q)
                l_idx = bisect.bisect_left(indexs, q)

                if q == indexs[0]:
                    ans.append(min(indexs[r_idx]-q,n-(indexs[-1]-q)))
                elif q == indexs[-1]:
                    ans.append(min(q - indexs[l_idx-1], n-q + indexs[0]))
                else:
                    ans.append(min(indexs[r_idx]-q, q - indexs[l_idx-1]))
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.solveQueries(nums = [1,3,1,4,1,3,2], queries = [0,3,5]) == [2,-1,3]
    assert obj.solveQueries(nums = [1,2,3,4], queries = [0,1,2,3]) == [-1,-1,-1,-1]
    assert obj.solveQueries(nums = [2,10,20,20,20], queries = [1,4,2]) == [-1,1,1]
    assert obj.solveQueries(nums = [6,12,17,9,16,7,6], queries = [5,6,0,4]) == [-1,1,1,-1]
