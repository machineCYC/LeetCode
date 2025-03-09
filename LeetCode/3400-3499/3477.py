'''
3477. Fruits Into Baskets II

2025.03.09 Sunday 20:12
'''
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        baskets_place_flag = [True] * n
        for fru in fruits:
            for idx, bask in enumerate(baskets):
                if fru <= bask and baskets_place_flag[idx]:
                    baskets_place_flag[idx] = False
                    break
        return sum(baskets_place_flag)


if __name__ == "__main__":
    obj = Solution()
    assert obj.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]) == 1
    assert obj.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]) == 0
