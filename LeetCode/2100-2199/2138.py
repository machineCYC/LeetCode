'''
2138. Divide a String Into Groups of Size k

2022.01.16 Sunday 12:57
'''
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        n = len(s)
        for i in range(0, n, k):
            sub_s = s[i:i+k]
            ns = len(sub_s)
            sub_s = sub_s if ns == k else (sub_s + (fill * (k - ns)))
            ans.append(sub_s)
        return ans

if __name__ == "__main__":
    obj = Solution()
    assert obj.divideString(s = "abcdefghi", k = 3, fill = "x")==["abc","def","ghi"]
    assert obj.divideString(s = "abcdefghij", k = 3, fill = "x")==["abc","def","ghi","jxx"]
