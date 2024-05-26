'''
3163. String Compression III

2024.05.26 Sunday 15:26
'''


class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        pre = None
        cur = None
        counting = {}
        for w in word+"@":
            cur = w
            if w not in counting:
                counting[w] = 1
            else:
                counting[w] += 1

            if pre is None:
                pre = cur
                continue

            if pre != cur:
                nbr = counting[pre]
                while nbr > 0:
                    if nbr <= 9:
                        ans += f"{nbr}{pre}"
                        counting[pre] = 0
                        nbr = 0
                    else:
                        ans += f"9{pre}"
                        nbr -= 9
            pre = cur
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.compressedString(word = "abcde") == "1a1b1c1d1e"
    assert obj.compressedString(word = "aaaaaaaaaaaaaabb") == "9a5a2b"
    assert obj.compressedString(word = "aabbaacc") == "2a2b2a2c"
    assert obj.compressedString(word = "dddddddddduuuuuuuuudddddddddtuuuuuuumhhooooooooobb") == "9d1d9u9d1t7u1m2h9o2b"

