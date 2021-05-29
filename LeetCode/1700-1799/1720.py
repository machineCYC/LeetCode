'''
1720. Decode XORed Array

2021.01.10 Sunday 15:07
'''
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first for i in range(len(encoded)+1)]
        for i, e in enumerate(encoded):
            ans[i+1] = e ^ ans[i]
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.decode(encoded = [1,2,3], first = 1)==[1,0,2,1]
    assert obj.decode(encoded = [6,2,7,3], first = 4)==[4,2,0,7,4]
