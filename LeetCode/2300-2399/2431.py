'''
2341. Maximum Number of Pairs in Array

2022.07.17 Sunday 13:30
'''
from typing import List
from collections import defaultdict


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        pairs_cnt = 0
        leftover_cnt = 0
        for k, v in count.items():
            pairs_cnt += v // 2
            leftover_cnt += v % 2
        return [pairs_cnt, leftover_cnt]

if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfPairs(nums = [1,3,2,1,3,2,2])==[3,1]
    assert obj.numberOfPairs(nums = [1,1])==[1,0]
    assert obj.numberOfPairs(nums = [0])==[0,1]
