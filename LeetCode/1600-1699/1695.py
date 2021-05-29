'''
1695. Maximum Erasure Value

2020.12.20 Sunday 13:17
'''
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cumsum = [0]
        for i in range(len(nums)):
            cumsum += [cumsum[-1] + nums[i]]

        pos = {}
        maxscore = 0
        left_index = 0
        for i, n in enumerate(nums):
            if n in pos:
                left_index = max(left_index, pos[n])
            pos[n] = i + 1
            maxscore = max(maxscore, cumsum[i+1]-cumsum[left_index])

        return maxscore

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumUniqueSubarray(nums = [4,2,4,5,6])==17
    assert obj.maximumUniqueSubarray(nums = [10000])==10000
    assert obj.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5])==8
    assert obj.maximumUniqueSubarray(nums=[4078,1065,3781,6541,304,9192,5474,3049,6281,385,1531,3194,7445,9453,6210,5165,6203,9272,6798,1719,6618,1580,3353,2387,5477,2289,8431,2653,6842,481,5777,4494,5935,7983,8983,9216,6897,3467,4598,6343,6429,7830,9543,1312,5491,5748,8252,4271,2345,1358,3924,741,1844,5695,322,3204,3815,1432,9226,3372,6007,3916,9402,5363,7240,9291,9821,3543,7215,3691,3149,5295,7813, 3049,710,6500,4893,7063,4647,6865,7190,2844,7508,6811,7719,2916,3496,9861,5385,5655])==428472
