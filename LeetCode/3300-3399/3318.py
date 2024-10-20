'''
3318. Find X-Sum of All K-Long Subarrays I

2024.10.20 Sunday 10:06
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)

        def xsum(array, x):
            counter = defaultdict(int)
            for n in array:
                counter[n] += 1
            scounter = sorted(counter.items(), key = lambda k: (k[1], k[0]), reverse=True)
            return sum([k*v for k,v in scounter[:x]])


        for idx in range(len(ans)):
            sub_array = nums[idx:idx+k]
            ans[idx] = xsum(sub_array, x)

        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2) == [6,10,12]
    assert obj.findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2) ==[11,15,15,15,12]
