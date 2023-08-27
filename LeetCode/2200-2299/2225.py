'''
2225. Find Players With Zero or One Losses

2022.04.03 Sunday 14:39
'''
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ret = dict()
        for w, l in matches:
            if l not in ret:
                ret[l] = []
            if w not in ret:
                ret[w] = []
            ret[l].append(w)

        not_lost = []
        lost_one = []
        for k in ret:
            lost_cnt = len(ret[k])
            if lost_cnt == 0:
                not_lost.append(k)

            if lost_cnt == 1:
                lost_one.append(k)
        return [sorted(not_lost), sorted(lost_one)]


if __name__ == "__main__":
    obj = Solution()
    assert obj.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
    assert obj.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]])
