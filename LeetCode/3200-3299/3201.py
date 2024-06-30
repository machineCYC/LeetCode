'''
3201. Find the Maximum Length of Valid Subsequence I

2024.06.30 Sunday 14:53
'''
from typing import List
from collections import defaultdict, Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        only have 4 cases need to calculate
        case1:
        init value is even and (sub[x - 2] + sub[x - 1]) % 2 == 0
        case2:
        init value is odd and (sub[x - 2] + sub[x - 1]) % 2 == 0
        case3:
        init value is even and (sub[x - 2] + sub[x - 1]) % 2 == 1
        case4:
        init value is odd and (sub[x - 2] + sub[x - 1]) % 2 == 1
        """
        mod_nums = [n % 2 for n in nums]
        n = len(mod_nums)

        if n == 2:
            return 2

        zero_odd_ans = 0
        cur = 1
        for idx, v in enumerate(mod_nums):
            if (cur+ v) % 2 == 0:
                cur = v
                zero_odd_ans += 1

        zero_even_ans = 0
        cur = 0
        for idx, v in enumerate(mod_nums):
            if (cur+ v) % 2 == 0:
                cur = v
                zero_even_ans += 1

        one_odd_ans = 0
        cur = 1
        for idx, v in enumerate(mod_nums):
            if (cur+ v) % 2 == 1:
                cur = v
                one_odd_ans += 1

        one_even_ans = 0
        cur = 0
        for idx, v in enumerate(mod_nums):
            if (cur+ v) % 2 == 1:
                cur = v
                one_even_ans += 1

        return max([zero_odd_ans, zero_even_ans, one_odd_ans, one_even_ans])


if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumLength(nums = [1,2,3,4]) == 4
    assert obj.maximumLength(nums = [1,2,1,1,2,1,2]) == 6
    assert obj.maximumLength(nums = [1,3]) == 2
    assert obj.maximumLength(nums = [4,2,6]) == 3
    assert obj.maximumLength(nums = [4,51,68]) == 3
    assert obj.maximumLength(nums = [1,2,1]) == 3
    assert obj.maximumLength(nums = [1,1,1]) == 3
    assert obj.maximumLength(nums = [2,2,2]) == 3
    assert obj.maximumLength(nums = [1,5,9,4,2]) == 3
