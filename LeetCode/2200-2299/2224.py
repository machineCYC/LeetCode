'''
2224. Minimum Number of Operations to Convert Time

2022.04.03 Sunday 14:34
'''


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_h, cur_m = current.split(":")
        cor_h, cor_m = correct.split(":")

        if cor_m >= cur_m:
            diff_mins = int(cor_m) - int(cur_m) + ( int(cor_h) - int(cur_h) ) * 60
        else:
            diff_mins = int(cor_m) - int(cur_m) + 60 + ( int(cor_h) - int(cur_h) -1 ) * 60

        ops_cnt = 0
        for ops in [60, 15, 5, 1]:
            ops_cnt += diff_mins // ops
            diff_mins = diff_mins % ops

        return ops_cnt

if __name__ == "__main__":
    obj = Solution()
    assert obj.convertTime(current = "02:30", correct = "04:35")==3
    assert obj.convertTime(current = "11:00", correct = "11:01")==1
