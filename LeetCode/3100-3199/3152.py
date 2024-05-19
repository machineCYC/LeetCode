'''
3152. Special Array II

2024.05.19 Sunday 14:41
'''
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        # def isSpecial(nums):
        #     n = len(nums)
        #     for i in range(1, n, 1):
        #         pre = nums[i-1]
        #         cur = nums[i]
        #         if cur % 2  == pre % 2:
        #             return False
        #     return True

        # ans = [isSpecial(nums[quer[0]:quer[1]+1]) for quer in queries]
        # return ans

        n = len(nums)
        cum_same_parity_cnt = [0] * n
        for i in range(1, n, 1):
            cum_same_parity_cnt[i] = cum_same_parity_cnt[i-1]
            if nums[i] % 2 == nums[i-1] % 2:
                cum_same_parity_cnt[i] += 1

        ans = []
        for query in queries:
            if cum_same_parity_cnt[query[1]] - cum_same_parity_cnt[query[0]] == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans



if __name__ == "__main__":
    obj = Solution()
    assert obj.isArraySpecial(nums = [10,2,10,9,7], queries = [[2,3]]) == [True]
    assert obj.isArraySpecial(nums = [5,1,4,7], queries = [[1,3]]) == [True]
    assert obj.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]) == [False]
    assert obj.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]) == [False, True]
    assert obj.isArraySpecial(nums = [5,1,5], queries = [[0,1]]) == [False]
