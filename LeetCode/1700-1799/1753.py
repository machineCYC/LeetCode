'''
1753. Maximum Score From Removing Stones

2021.02.07 Sunday 14:40
'''


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = [a, b, c]
        snums = sorted(nums)

        n_a, n_b, n_c = snums
        ret = 0
        for i in range(n_a+1):
            set_b = i
            set_c = n_a - i

            score = n_a + min(n_b-set_b, n_c-set_c)
            ret = max(ret, score)

        return ret

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumScore(a = 2, b = 4, c = 6) == 6
    assert obj.maximumScore(a = 4, b = 4, c = 6 == 7
    assert obj.maximumScore(a = 1, b = 8, c = 8) == 8
