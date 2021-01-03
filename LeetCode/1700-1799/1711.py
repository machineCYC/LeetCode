'''
1711. Count Good Meals

2021.01.03 Sunday 13:59
'''
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import defaultdict
        freq = defaultdict(int)

        count = 0
        n = len(deliciousness)
        for d in deliciousness:
            for k in range(22):
                count += freq[2**k - d]
            freq[d] += 1
        return int(count % (10**9 + 7))


if __name__ == "__main__":
    obj = Solution()
    assert obj.countPairs(deliciousness=[1,3,5,7,9])==4
    assert obj.countPairs(deliciousness=[1,1,1,3,3,3,7])==15
    assert obj.countPairs(deliciousness=[2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468])==53
