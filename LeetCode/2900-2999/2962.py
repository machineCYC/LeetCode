'''
2962. Count Subarrays Where Max Element Appears at Least K Times

2023.12.10 Sunday 14:43
'''
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # # too slow
        # max_v = max(nums)
        # n = len(nums)
        # cum_max_value_cnt = [1 if num==max_v else 0 for num in nums]
        # ans = 0
        # for i in range(n):
        #     for j in range(i+ k-1, n):
        #         if sum(cum_max_value_cnt[i:j+1]) >= k:
        #             ans += 1
        # return ans

        ans = 0
        max_v = max(nums)
        cnt = 0
        idy = 0
        for idx, v in enumerate(nums):
            if v == max_v:
                cnt += 1

            while cnt >= k:
                cnt -= nums[idy] == max_v
                idy += 1
            ans += idy
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countSubarrays(nums = [1,3,2,3,3], k = 2) == 6
    assert obj.countSubarrays(nums = [1,4,2,1], k = 3) == 0
    assert obj.countSubarrays(nums = [28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49], k = 1) == 187
