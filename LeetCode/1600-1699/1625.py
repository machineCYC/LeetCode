'''
1625. Lexicographically Smallest String After Applying Operations

2020.10.18 Sunday 12:43
'''


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_odd_index(s, a):
            for i in range(1, len(s), 2):
                s = s[:i] + str((int(s[i]) + a) % 10) + s[i+1:]
            return s

        def rotate_right(s, b):
            return s[len(s)-b:]+s[:len(s)-b]

        seen = set()
        need = list()
        need.append(s)

        while need:
            curr = need.pop()
            if curr not in seen:
                seen.add(curr)
                s_add = add_odd_index(curr, a)
                s_rota = rotate_right(curr, b)
                need.extend([s_add, s_rota])
        return min(seen)

if __name__ == "__main__":
    obj = Solution()
    assert obj.findLexSmallestString(s = "5525", a = 9, b = 2) == "2050"
    assert obj.findLexSmallestString(s = "74", a = 5, b = 1) == "24"
    assert obj.findLexSmallestString(s = "0011", a = 4, b = 2) == "0011"
    assert obj.findLexSmallestString(s = "43987654", a = 7, b = 3) == "00553311"
