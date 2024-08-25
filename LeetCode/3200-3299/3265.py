'''
3265. Count Almost Equal Pairs I

2024.08.25 Sunday 13:29
'''
from typing import List
from collections import defaultdict, Counter, OrderedDict


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def get_possible_forms(num):
            num_str = str(num)
            n = len(num_str)
            forms = set()
            forms.add(num)

            # Generate all possible forms by swapping any two digits
            for i in range(n):
                for j in range(i + 1, n):
                    # Swap digits at positions i and j
                    swapped = list(num_str)
                    swapped[i], swapped[j] = swapped[j], swapped[i]
                    forms.add(int(''.join(swapped)))

            return forms

        count = 0
        n = len(nums)
        for i in range(n):
            forms_i = get_possible_forms(nums[i])
            for j in range(i + 1, n):
                if nums[j] in forms_i or nums[i] in get_possible_forms(nums[j]):
                    count += 1

        return count


if __name__ == "__main__":
    obj = Solution()
    assert obj.countPairs(nums = [3,12,30,17,21]) == 2
    assert obj.countPairs(nums = [1,1,1,1,1]) == 10
    assert obj.countPairs(nums = [123,231]) == 0
