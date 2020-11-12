'''
1647. Minimum Deletions to Make Character Frequencies Unique

2020.11.08 Sunday 15:00
'''

class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        for i in s:
            count[i] = 1 + count.get(i, 0)

        ans = 0
        seen = set()
        for c in sorted(count.values(), reverse=True):
            while c in seen:
                c -= 1
                ans += 1

            if c:
                seen.add(c)
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.minDeletions(s = "aab")==0
    assert obj.minDeletions(s = "aaabbbcc")==2
    assert obj.minDeletions(s = "ceabaacb")==2
