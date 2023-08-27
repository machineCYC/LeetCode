'''
1887. Reduction Operations to Make the Array Elements Equal

2021.06.06 Sunday 14:43
'''
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sort_set_list = sorted(list(set(nums)))
        value_index_dict = {}
        for i, n in enumerate(sort_set_list):
            value_index_dict[n] = i

        count = 0
        for n in nums:
            n_index = value_index_dict.get(n)
            count += n_index
        return count


if __name__ == "__main__":
    obj = Solution()
    assert obj.reductionOperations(nums = [5,1,3]) == 3
    assert obj.reductionOperations(nums = [1,1,1]) == 0
    assert obj.reductionOperations(nums = [1,1,2,2,3]) == 4