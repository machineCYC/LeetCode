'''
2835. Minimum Operations to Form Subsequence With Target Sum

2023.08.27 Sunday 14:56
'''
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1

        opcnt = 0
        nums.sort()
        while True:
            total = 0
            for idx in range(len(nums)-1, -1, -1):
                if nums[idx] + total > target:
                    skip_idx = idx
                    continue
                total += nums[idx]
            if total == target:
                break
            else:
                cut = nums.pop(skip_idx) // 2
                nums.extend([cut, cut])
                nums.sort()
                opcnt += 1
        return opcnt



if __name__ == "__main__":
    obj = Solution()
    assert obj.minOperations(nums = [1,2,8], target = 7)==1
    assert obj.minOperations(nums = [1,32,1,2], target = 12)==2
    assert obj.minOperations(nums = [1,32,1], target = 35)==-1
    assert obj.minOperations(nums = [128,1,128,1,64], target = 4)==4
    assert obj.minOperations(nums = [1,1,128,256,1,16], target = 5)==2