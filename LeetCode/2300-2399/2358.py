'''
2358. Maximum Number of Groups Entering a Competition

2022.08.01 Monday 19:49
'''
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades = sorted(grades)

        cnt = 1
        last_group_sum = grades[0]
        last_group_cnt = 1
        group_sum = 0
        group_cnt = 0
        for i, g in enumerate(grades):
            if i:
                group_sum += g
                group_cnt += 1

                if group_sum > last_group_sum and group_cnt>last_group_cnt:
                    last_group_sum = group_sum
                    last_group_cnt = group_cnt
                    group_sum = 0
                    group_cnt = 0
                    cnt += 1

        return cnt

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumGroups(grades = [10,6,12,7,3,5])==3
    assert obj.maximumGroups(grades = [8,8])==1
