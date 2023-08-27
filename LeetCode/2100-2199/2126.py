'''
2126. Destroying Asteroids

2022.01.02 Sunday 17:30
'''
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sort_asteroids = sorted(asteroids)

        for a in sort_asteroids:
            if a <= mass:
                mass += a
            else:
                return False
        return True


if __name__ == "__main__":
    obj = Solution()
    assert obj.asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21])==True
    assert obj.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4])==False
    assert obj.asteroidsDestroyed(mass = 1, asteroids = [1])==True