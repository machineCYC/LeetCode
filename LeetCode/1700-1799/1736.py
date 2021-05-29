'''
1736. Latest Time by Replacing Hidden Digits

2021.01.24 Sunday 16:17
'''


class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i, t in enumerate(time):
            if t == '?':
                if i == 0:
                    time[i] = "2" if time[1] in "?0123" else "1"
                elif i == 1:
                    time[i] = "3" if time[0] == "2" else "9"
                elif i == 3:
                    time[i] = "5"
                elif i == 4:
                    time[i] = "9"
        return "".join(time)

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumTime(time = "2?:?0")=="23:50"
    assert obj.maximumTime(time = "0?:3?")=="09:39"
    assert obj.maximumTime(time = "1?:22")=="19:22"
    assert obj.maximumTime(time = "00:01")=="00:01"
    assert obj.maximumTime(time = "04:?9")=="04:59"
