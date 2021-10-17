'''
2042. Check if Numbers Are Ascending in a Sentence

2021.10.17 Sunday 12:16
'''


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nbr = 0
        for i in s.split(" "):
            if i.isdigit():
                if int(i)>nbr:
                    nbr = int(i)
                else:
                    return False
        return True

if __name__ == "__main__":
    obj = Solution()
    assert obj.areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles")==True
    assert obj.areNumbersAscending(s = "hello world 5 x 5")==False
    assert obj.areNumbersAscending(s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")==False
    assert obj.areNumbersAscending(s = "4 5 11 26")==True
