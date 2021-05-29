'''
1806. Minimum Number of Operations to Reinitialize a Permutation

2021.03.21 Sunday 13:25
'''


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        prem = [i for i in range(n)]
        arr = [i for i in range(n)]
        count = 0
        while True:
            arr = [arr[i // 2]  if i % 2 == 0 else arr[n // 2 + (i - 1) // 2] for i in range(n)]

            count += 1
            if arr == prem and count!=0:
                return count

if __name__ == "__main__":
    obj = Solution()
    assert obj.reinitializePermutation(n=2) == 1
    assert obj.reinitializePermutation(n=4) == 2
    assert obj.reinitializePermutation(n=6) == 4
