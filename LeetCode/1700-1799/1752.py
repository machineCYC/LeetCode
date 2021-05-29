'''
1752. Check if Array Is Sorted and Rotated

2021.02.07 Sunday 13:46
'''
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        def check_sort(nums):
            n = len(nums)
            for j in range(1, n):
                if tmp_nums[j] < tmp_nums[j-1]:
                    return False
            return True

        for i in range(n):
            tmp_nums = nums[i:] + nums[:i]
            ret = check_sort(tmp_nums)

            if ret:
                return True
        return False


if __name__ == "__main__":
    obj = Solution()
    assert obj.check(nums = [3,4,5,1,2]) == True
    assert obj.check(nums = [2,1,3,4]) == False
    assert obj.check(nums = [1,2,3]) == True
    assert obj.check(nums = [1,1,1]) == True
    assert obj.check(nums = [2,1]) == True
