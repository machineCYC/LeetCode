'''
2073. Time Needed to Buy Tickets

2021.11.04 Sunday 13:18
'''
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        i = 0
        sec = 0
        while True:
            j = i % n
            if tickets[j] != 0:
                tickets[j] -= 1
                sec += 1
                if tickets[k] == 0:
                    break
            i += 1
        return sec


if __name__ == "__main__":
    obj = Solution()
    assert obj.timeRequiredToBuy(tickets = [2,3,2], k = 2) == 6
    assert obj.timeRequiredToBuy(tickets = [5,1,1,1], k = 0) == 8