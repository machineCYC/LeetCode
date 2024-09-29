'''
3304. Find the K-th Character in String Game I

2024.09.29 Sunday 12:50
'''


class Solution:
    def kthCharacter(self, k: int) -> str:
        cur = "a"
        pre = "a"
        if k == 1:
            return "a"

        for i in range(k):
            if len(cur) >= k:
                return cur[k-1]
            cur += "".join([chr(ord(e) + 1 if ord(e)<122 else 97) for e in pre])
            pre = cur


if __name__ == "__main__":
    obj = Solution()
    assert obj.kthCharacter(k = 1) == "a"
    assert obj.kthCharacter(k = 3) == "b"
    assert obj.kthCharacter(k = 5) == "b"
    assert obj.kthCharacter(k = 10) == "c"
