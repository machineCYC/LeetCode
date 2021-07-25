'''
1946. Largest Number After Mutating Substring

2021.07.25 Sunday 14:41
'''
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        maping = {}
        for i in num:
            maping[i] = change[int(i)]

        ret = ""
        isfirstbigger = False
        for i, n in enumerate(num):
            if maping[n] > int(n):
                ret += str(maping[n])
                isfirstbigger = True
            elif maping[n] == int(n):
                ret += str(maping[n])
            else:
                if isfirstbigger:
                    return ret + num[i:]
                ret += n
        return ret


if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumNumber(num = "132", change = [9,8,5,0,3,6,4,2,6,8])=="832"
    assert obj.maximumNumber(num = "021", change = [9,4,3,5,7,2,1,9,0,6])=="934"
    assert obj.maximumNumber(num = "5", change = [1,4,7,5,3,2,5,6,9,4])=="5"
    assert obj.maximumNumber(num = "214010", change = [6,7,9,7,4,0,3,4,4,7])=="974676"
    assert obj.maximumNumber(num = "334111", change = [0,9,2,3,3,2,5,5,5,5])=="334999"
