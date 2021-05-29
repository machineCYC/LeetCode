'''
1624. Largest Substring Between Two Equal Characters

2020.10.18 Sunday 12:54
'''


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = dict()
        for ss in s:
            if ss in count:
                count[ss] += 1
            else:
                count[ss] = 1

        have_two_characters = [k for k in count if count[k]>1 ]
        if len(have_two_characters) == 0:
            return -1
        else:
            ret = []
            for c in have_two_characters:

                c_index = [i for i, ss in enumerate(s) if ss == c]
                first_index = min(c_index)
                last_index = max(c_index)
                conti_chars = max(last_index - first_index - 1, 0)
                ret.append(conti_chars)
            return max(ret)

if __name__ == "__main__":
    obj = Solution()
    assert obj.maxLengthBetweenEqualCharacters(s = "aa")==0
    assert obj.maxLengthBetweenEqualCharacters(s = "abca")==2
    assert obj.maxLengthBetweenEqualCharacters(s = "cbzxy")==-1
    assert obj.maxLengthBetweenEqualCharacters(s = "cabbac")==4
