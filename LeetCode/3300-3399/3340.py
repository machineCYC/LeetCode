'''
3340. Check Balanced String

2024.11.03 Sunday 16:49
'''


class Solution:
    def isBalanced(self, num: str) -> bool:
        a = 0
        e = 0
        for i, n in enumerate(num):
            if  i % 2 == 0:
                e += int(n)
            else:
                a += int(n)

        return a == e


if __name__ == "__main__":
    obj = Solution()
    assert obj.isBalanced(num = "1234") == False
    assert obj.isBalanced(num = "24123") == True
