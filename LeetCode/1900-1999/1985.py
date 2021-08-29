'''
1985. Find the Kth Largest Integer in the Array

2021.08.29 Sunday 14:18
'''
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_nums = [int(n) for n in nums]
        int_nums.sort()
        return str(int_nums[-k])


if __name__ == "__main__":
    obj = Solution()
    assert obj.kthLargestNumber(nums = ["3","6","7","10"], k = 4) == "3"
    assert obj.kthLargestNumber(nums = ["2","21","12","1"], k = 3) == "2"
    assert obj.kthLargestNumber(nums = ["0","0"], k = 2) == "0"
