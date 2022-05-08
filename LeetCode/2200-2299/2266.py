'''
2266. Count Number of Texts

2022.05.08 Sunday 21:00
'''


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = pow(10, 9) + 7
        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1
        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i-1] % mod
            if i-2 >= 0 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] += dp[i-2]
            if i-3 >= 0 and pressedKeys[i-1] == pressedKeys[i-2] and pressedKeys[i-1] == pressedKeys[i-3]:
                dp[i] += dp[i-3]

            if pressedKeys[i-1] in "79":
                if i - 4 >= 0 and pressedKeys[i-1] == pressedKeys[i-2] and pressedKeys[i-1] == pressedKeys[i-3] and pressedKeys[i-1] == pressedKeys[i-4]:
                    dp[i] += dp[i-4]
        return dp[-1] % mod


if __name__ == "__main__":
    obj = Solution()
    assert obj.countTexts(pressedKeys = "22233") == 8
    assert obj.countTexts(pressedKeys = "222222222222222222222222222222222222") == 82876089
