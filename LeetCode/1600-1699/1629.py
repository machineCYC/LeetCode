'''
1629. Slowest Key

2020.10.25 Sunday 14:16
'''
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        for i in range(n):
            if i == 0:
                t_duration = releaseTimes[0]
                k_longest = keysPressed[0]
            else:
                new_t_duration = releaseTimes[i] - releaseTimes[i-1]
                k_new = keysPressed[i]
                if new_t_duration > t_duration:
                    k_longest = k_new
                    t_duration = new_t_duration
                elif new_t_duration == t_duration:
                    k_longest = max(k_longest, k_new)
                    t_duration = new_t_duration

        return k_longest

if __name__ == "__main__":
    obj = Solution()
    assert obj.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")=="c"
    assert obj.slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda")=="a"
    assert obj.slowestKey(releaseTimes = [23,34,43,59,62,80,83,92,97],keysPressed = "qgkzzihfc")=="q"
