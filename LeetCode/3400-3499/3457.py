'''
3457. Eat Pizzas!

2025.02.16 Sunday 14:10
'''
from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        groups = n // 4
        topn = groups // 2
        if groups % 2 == 1:
            topn += 1
        rem = pizzas[:-1 * topn]
        ans = sum(pizzas[-1 * topn :])
        print(rem)
        for _ in range(groups - topn):
            v1 = rem.pop()
            v2 = rem.pop()
            ans += v2
        print(ans)
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxWeight(pizzas = [1,2,3,4,5,6,7,8]) == 14
    assert obj.maxWeight(pizzas = [2,1,1,1,1,1,1,1]) == 3
    assert obj.maxWeight(pizzas = [1,2,3,4,5,6,7,8,9,10,11,12]) == 32
    assert obj.maxWeight(pizzas = [5,2,2,4,3,3,1,3,2,5,4,2]) == 14