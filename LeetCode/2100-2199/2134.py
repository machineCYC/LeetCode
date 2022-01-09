'''
2134. Minimum Swaps to Group All 1's Together II

2022.01.09 Sunday 15:06
'''
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        nums = nums + nums
        n = len(nums)
        onesinwindows = 0
        maxonesinwindows = 0
        for j in range(n):
            if j >= ones and nums[j-ones] == 1:
                onesinwindows -= 1

            if nums[j]:
                onesinwindows += 1

            maxonesinwindows = max(maxonesinwindows, onesinwindows)


        return(ones - maxonesinwindows)


if __name__ == "__main__":
    obj = Solution()
    assert obj.minSwaps(nums = [0,1,0,1,1,0,0])==1
    assert obj.minSwaps(nums = [0,1,1,1,0,0,1,1,0])==2
    assert obj.minSwaps(nums = [1,1,0,0,1])==0
