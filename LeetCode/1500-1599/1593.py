'''
1593. Split a String Into the Max Number of Unique Substrings

2020.09.20 Sunday 16:51

Backtracking
'''

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(s, seen):
            ans = 0
            if s:
                for i in range(1, len(s)+1, 1):
                    substring = s[:i]
                    if substring not in seen:
                        seen.add(substring)
                        ans = max(ans, 1+helper(s[i:], seen))
                        seen.remove(substring)
            return ans

        seen = set()
        ans = helper(s, seen)
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.maxUniqueSplit(s = "ababccc")==5
    assert obj.maxUniqueSplit(s = "aba")==2
    assert obj.maxUniqueSplit(s = "aa")==1