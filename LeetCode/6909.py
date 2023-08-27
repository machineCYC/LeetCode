'''
6916. Prime Pairs With Target Sum

2023.07.02 Sunday 14:26
'''
from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                cnt = 1
                for j in range(i+1, len(nums), 1):
                    if nums[j] % 2 != nums[j-1] % 2 and nums[j] <= threshold:
                        cnt += 1
                    else:
                        break
                ans = max(ans, cnt)
        return ans



if __name__ == "__main__":
    obj = Solution()
    assert obj.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5) == 3
    assert obj.longestAlternatingSubarray(nums = [1,2],threshold = 2) == 1
    assert obj.longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4) == 3
    assert obj.longestAlternatingSubarray(nums = [4], threshold = 1) == 0
    assert obj.longestAlternatingSubarray(nums = [4,10,3], threshold = 10) == 2