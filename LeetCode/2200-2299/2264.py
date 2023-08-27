'''
2264. Largest 3-Same-Digit Number in String

2022.05.28 Sunday 16:31
'''


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        n = len(num)
        for i in range(2, n):
            if num[i] == num[i-1] and num[i-1] == num[i-2]:
                max_good = max(max_good, num[i-2:i+1])
        return max_good

if __name__ == "__main__":
    obj = Solution()
    assert obj.largestGoodInteger(num = "6777133339")=="777"
    assert obj.largestGoodInteger(num = "2300019")=="000"
    assert obj.largestGoodInteger(num = "42352338")==""