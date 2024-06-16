'''
3184. Count Pairs That Form a Complete Day I

2024.06.16 Sunday 14:42
'''
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        n = len(hours)
        for i in range(n):
            for j in range(i+1, n):
                total_hours = hours[i] + hours[j]
                if total_hours % 24 == 0:
                    ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countCompleteDayPairs(hours = [12,12,30,24,24]) == 2
    assert obj.countCompleteDayPairs(hours = [72,48,24,3]) == 3
