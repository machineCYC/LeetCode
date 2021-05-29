'''
1630. Arithmetic Subarrays

2020.10.25 Sunday 14:23
'''
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(array):
            n = len(array)

            diff = array[1] - array[0]
            for i in range(2, n, 1):
                cur = array[i]
                bef = array[i-1]
                if diff != (cur-bef):
                    return False
            return True


        ans = []
        for ll, rr in zip(l, r):
            subarray = nums[ll: rr+1]
            sort_subarray = sorted(subarray)
            bool_arithmetic = is_arithmetic(sort_subarray)
            ans.append(bool_arithmetic)

        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])==[True,False,True]
    assert obj.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])==[False,True,False,False,True,True]
