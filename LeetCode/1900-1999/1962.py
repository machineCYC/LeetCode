'''
1962. Remove Stones to Minimize the Total

2021.08.08 Sunday 13:46
'''
from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        item = [-p for p in piles]
        heapq.heapify(item)
        for i in range(k):
            nigative_maxv = (item[0] * -1) // 2
            heapq.heapreplace(item, item[0] + nigative_maxv)

        return -1*sum(item)


if __name__ == "__main__":
    obj = Solution()
    assert obj.minStoneSum(piles = [5,4,9], k = 2) == 12
    assert obj.minStoneSum(piles = [4,3,6,7], k = 3) == 12
