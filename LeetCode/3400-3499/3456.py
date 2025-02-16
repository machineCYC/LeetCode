'''
3456. Find Special Substring of Length K

2025.02.16 Sunday 13:31
'''


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = 1
        n = len(s)
        if n == 1:
            return True

        for idx in range(1, n):
            before = s[idx-1]
            if s[idx] == before:
                count += 1
            else:
                if k == 1 and idx == 1:
                    return True
                count = 1

            if idx + 1 < n:
                if count == k and s[idx+1] != s[idx]:
                    return True
            elif idx + 1 == n:
                if count == k:
                    return True
        return False


if __name__ == "__main__":
    obj = Solution()
    assert obj.hasSpecialSubstring(s = "aaabaaa", k = 3) == True
    assert obj.hasSpecialSubstring(s = "abc", k = 2) == False
    assert obj.hasSpecialSubstring(s = "aaaab", k = 3) == False
    assert obj.hasSpecialSubstring(s = "aaaab", k = 1) == True
    assert obj.hasSpecialSubstring(s = "h", k = 1) == True
    assert obj.hasSpecialSubstring(s = "dii", k = 1) == True
