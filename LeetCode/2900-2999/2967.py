'''
2967. Minimum Cost to Make Array Equalindromic

2023.12.17 Sunday 16:03
'''
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        def is_palindromic(num: int) -> bool:
            return str(num) == str(num)[::-1]

        def calculate_cost(mid:int):
            return sum([abs(mid-i)for i in nums])

        left_mid = -1
        right_mid = -1
        ans = 10**15
        nums.sort()
        n = len(nums)
        mid = n // 2
        if is_palindromic(nums[mid]):
            ans = calculate_cost(nums[mid])
        else:
            is_find_left = False
            is_find_right = False
            left = nums[mid] - 1
            right = nums[mid] + 1
            while not (is_find_left) or (not is_find_right):
                if is_palindromic(left):
                    left_mid = left
                    is_find_left = True
                else:
                    left -= 1

                if is_palindromic(right):
                    right_mid = right
                    is_find_right = True
                else:
                    right += 1
        return min(ans, min(calculate_cost(left_mid), calculate_cost(right_mid)))





if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumCost(nums = [1,2,3,4,5]) == 6
    assert obj.minimumCost(nums = [10,12,13,14,15]) == 11
    assert obj.minimumCost(nums = [22,33,22,33,22]) == 22
