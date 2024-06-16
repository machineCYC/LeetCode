'''
3185. Count Pairs That Form a Complete Day II

2024.06.16 Sunday 14:43
'''
from typing import List
from collections import defaultdict


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # Dictionary to count frequencies of remainders
        remainder_count = defaultdict(int)
        total_pairs = 0

        for hour in hours:
            remainder = hour % 24

            # Complement remainder to make the sum a multiple of 24
            if remainder == 0:
                complement = 0
            else:
                complement = 24 - remainder

            # Add the count of complements seen so far to the total pairs
            total_pairs += remainder_count[complement]

            # Update the frequency of the current remainder
            remainder_count[remainder] += 1

        return total_pairs


if __name__ == "__main__":
    obj = Solution()
    assert obj.countCompleteDayPairs(hours = [12,12,30,24,24]) == 2
    assert obj.countCompleteDayPairs(hours = [72,48,24,3]) == 3
