'''
2020.09.06 Sunday 13:27
'''

class Solution:
    def modifyString(self, s: str) -> str:
        s_new = ""

        for i in range(len(s)):
            alphas = [chr(i) for i in range(97, 123, 1)]
            if s[i] == "?":
                if i-1>=0 and s[i-1]!="?" and s[i-1] in alphas:
                    alphas.remove(s[i-1])

                if i+1<len(s) and s[i+1]!="?" and s[i+1] in alphas:
                    alphas.remove(s[i+1])

                if s[i-1] == "?" and i>0 and s_new[i-1] in alphas:
                    alphas.remove(s_new[i-1])

                s_new += alphas[0]
            else:
                s_new += s[i]
        return s_new

if __name__ == "__main__":
    obj = Solution()
    assert obj.modifyString(s = "?zs")=="azs"
    assert obj.modifyString(s = "ubv?w")=="ubvaw"
    assert obj.modifyString(s = "j?qg??b")=="jaqgacb"
    assert obj.modifyString(s = "??yw?ipkj?")=="abywaipkja"
    assert obj.modifyString(s = "?ob?b???")=="aobababa"
