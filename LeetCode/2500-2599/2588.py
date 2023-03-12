from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        dp = Counter({0: 1})
        res = pre = 0
        for a in nums:
            pre ^= a
            res += dp[pre]
            dp[pre] += 1
        return res

    def beautifulSubarrays_Bruteforce(self, nums: List[int]) -> int:
        # too slow
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                subnums = nums[i:j+1]
                if reduce(lambda x, y: x ^ y, subnums) == 0:
                    count += 1
        return count

if __name__ == "__main__":
    obj = Solution()
    assert obj.beautifulSubarrays(nums = [4,3,1,2,4]) == 2
    assert obj.beautifulSubarrays(nums = [1,10,4]) == 0
    assert obj.beautifulSubarrays(nums = [0]) == 1
    assert obj.beautifulSubarrays(nums = [1]) == 0
    assert obj.beautifulSubarrays(nums = [0, 0]) == 3
    assert obj.beautifulSubarrays_Bruteforce(nums = [4,3,1,2,4]) == 2
    assert obj.beautifulSubarrays_Bruteforce(nums = [1,10,4]) == 0
    assert obj.beautifulSubarrays_Bruteforce(nums = [0]) == 1
    assert obj.beautifulSubarrays_Bruteforce(nums = [1]) == 0
    assert obj.beautifulSubarrays_Bruteforce(nums = [0, 0]) == 3
