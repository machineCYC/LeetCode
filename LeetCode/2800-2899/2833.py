'''
2833. Furthest Point From Origin

2023.08.27 Sunday 14:20
'''

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        ans = 0
        both = 0
        for i, e in enumerate(moves):
            if moves[i] == "L":
                ans -= 1
            elif moves[i] == "R":
                ans += 1
            else:
                both += 1
        return abs(ans) + both


if __name__ == "__main__":
    obj = Solution()
    assert obj.furthestDistanceFromOrigin(moves = "L_RL__R")==3
    assert obj.furthestDistanceFromOrigin(moves = "_R__LL_")==5
    assert obj.furthestDistanceFromOrigin(moves = "_______")==7