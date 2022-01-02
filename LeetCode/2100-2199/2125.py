'''
2125. Number of Laser Beams in a Bank

2022.01.02 Sunday 17:20
'''
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for r in bank:
            c = r.count("1")
            if c:
                ans += prev * c
                prev = c
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfBeams(bank = ["011001","000000","010100","001000"])==8
    assert obj.numberOfBeams(bank = ["000","111","000"])==0