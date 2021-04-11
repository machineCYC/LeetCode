'''
1823. Find the Winner of the Circular Game

2021.04.11 Sunday 23:40
'''


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(n))
        drop_i = 0
        while len(nums) > 1:
            drop_i = (drop_i + k - 1) % len(nums)
            nums.pop(drop_i)

        return nums[-1] + 1


if __name__ == "__main__":
    obj = Solution()
    assert obj.findTheWinner(n = 5, k = 2)==3
    assert obj.findTheWinner(n = 6, k = 5)==1
    assert obj.findTheWinner(n = 5, k = 4)==1
