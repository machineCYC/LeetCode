'''
6909. Longest Even Odd Subarray With Threshold

2023.07.02 Sunday 14:35
'''
from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime  = [True] * (n + 1)
        is_prime [0] = is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n+1, p):
                    is_prime[i] = False
            p += 1

        ans = []
        for i in range(2, n // 2 + 1, 1):
            if is_prime[i] and is_prime[n-i]:
                ans.append([i, n-i])
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.findPrimePairs(n=10) == [[3,7],[5,5]]
    assert obj.findPrimePairs(n=2) == []
    assert obj.findPrimePairs(n=11) == []
    assert obj.findPrimePairs(n=3) == []