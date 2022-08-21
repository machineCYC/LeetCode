'''
2384. Largest Palindromic Number

2022.08.21 Sunday 20:25
'''
from collections import defaultdict


class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt_num = defaultdict(int)
        for n in num:
            cnt_num[n] += 1

        ans = ''.join(cnt_num[i] // 2 * i for i in "9876543210").lstrip("0")
        mid = max(cnt_num[i] % 2 * i for i in cnt_num)
        return ans + mid + ans[::-1] or "0"

if __name__ == "__main__":
    obj = Solution()
    assert obj.largestPalindromic(num = "444947137")=="7449447"
    assert obj.largestPalindromic(num = "00009")=="9"
    assert obj.largestPalindromic(num = "00001105")=="1005001"
    assert obj.largestPalindromic(num = "0009")=="9"
    assert obj.largestPalindromic(num = "00000")=="0"
    assert obj.largestPalindromic(num = "0000")=="0"