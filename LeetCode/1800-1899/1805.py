'''
1805. Number of Different Integers in a String

2021.03.28 Sunday 13:17
'''

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        d = ""
        for s in word:
            if s.isdigit():
                d += s
            else:
                d += " "

        return len(set(map(int, d.split())))

if __name__ == "__main__":
    obj = Solution()
    assert obj.numDifferentIntegers(word = "a123bc34d8ef34")==3
    assert obj.numDifferentIntegers(word = "leet1234code234")==2
    assert obj.numDifferentIntegers(word = "a1b01c001")==1
