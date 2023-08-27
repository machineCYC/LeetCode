'''
1898. Maximum Number of Removable Characters

2021.06.13 Sunday 18:29
'''
from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        m = len(p)

        def check(k):
            remove = set(removable[:k+1])
            i = 0
            j = 0
            while i < n and j < m:
                if i in remove:
                    i += 1
                    continue

                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == m

        res = 0
        l = 0
        r = len(removable) - 1
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                res = max(res, mid+1)
                l = mid + 1
            else:
                r = mid - 1
        return res

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]) == 2
    assert obj.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]) == 1
    assert obj.maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4]) == 0
    assert obj.maximumRemovals(s = "qobftgcueho", p = "obue", removable = [5,3,0,6,4,9,10,7,2,8]) == 7
