'''
1784. Check if Binary String Has at Most One Segment of Ones

2021.03.07 Sunday 13:40
'''


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        nbr = len(s)

        cnt = 0
        for i in range(1, nbr):
            if s[i] != s[i-1]:
                cnt += 1

        if cnt == 1:
            return True
        elif cnt == 0 and s[0] == '1':
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    assert obj.checkOnesSegment(s="1001") == False
    assert obj.checkOnesSegment(s="110") == True
    assert obj.checkOnesSegment(s="10101010101010") == False
    assert obj.checkOnesSegment(s="101010101010101011") == False
    assert obj.checkOnesSegment(s="1") == True
    assert obj.checkOnesSegment(s="10") == True
    assert obj.checkOnesSegment(s="1000") == True