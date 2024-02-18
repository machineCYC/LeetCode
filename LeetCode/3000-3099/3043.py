'''
6916. Prime Pairs With Target Sum

2023.07.02 Sunday 14:26
'''
from typing import List
import os

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # # too slow
        # def CommonPrefix(str1:str, str2:str) -> int:
        #     cnt = 0
        #     n = len(str1)
        #     m = len(str2)
        #     base = str2 if m < n else str1
        #     compar = str1 if m < n else str2
        #     for i in range(min(m, n)):
        #         if compar.startswith(base[:i+1]):
        #             cnt += 1
        #         else:
        #             break
        #     return cnt

        # ans = 0
        # for i in arr1:
        #     for j in arr2:
        #         ans = max(ans, CommonPrefix(str(i), str(j)))
        # return ans

        # # too slow
        # ans = 0
        # for i in arr1:
        #     for j in arr2:
        #         ans = max(ans, len(os.path.commonprefix((str(i), str(j)))))
        # return ans

        # # Brute Force
        # prefix1 = set()
        # for s in arr1:
        #     while s > 0:
        #         prefix1.add(s)
        #         s = s // 10

        # prefix2 = set()
        # for s in arr2:
        #     while s > 0:
        #         prefix2.add(s)
        #         s = s // 10

        # ans = 0
        # for e in prefix1:
        #     if e in prefix2:
        #         ans = max(ans, len(str(e)))
        # return ans

        # Sorting + 2-pointer
        arr1_str = [str(x) for x in arr1]
        arr2_str = [str(x) for x in arr2]

        arr1_str.sort(key = lambda x: (x, len(x)), reverse=True)
        arr2_str.sort(key = lambda x: (x, len(x)), reverse=True)

        i = j = 0
        ans = 0
        while i < len(arr1_str) and j < len(arr2_str):
            s1 = arr1_str[i]
            s2 = arr2_str[j]

            for k in range(min(len(s1), len(s2))):
                if s1[k] > s2[k]:
                    i += 1
                    break
                elif s1[k] < s2[k]:
                    j += 1
                    break
                else:
                    ans = max(ans, k+1)

            if s1[k] == s2[k]:
                i += 1
                j += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.longestCommonPrefix(arr1 = [5655359], arr2 = [56554]) == 4
    assert obj.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]) == 3
    assert obj.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]) == 0
