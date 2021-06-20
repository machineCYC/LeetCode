'''
1904. The Number of Full Rounds You Have Played

2021.06.20 Sunday 16:35
'''


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:

        def get_timestep(strTime):
            hh, mm = strTime.split(":")
            timestep = int(hh)*60 + int(mm)
            return timestep

        s_timestep = get_timestep(startTime)
        f_timestep = get_timestep(finishTime)

        if s_timestep > f_timestep:
            return self.numberOfRounds(startTime, '24:00') + self.numberOfRounds('00:00', finishTime)

        return f_timestep // 15 - (s_timestep // 15 + (s_timestep % 15 > 0))


if __name__ == "__main__":
    obj = Solution()
    assert obj.numberOfRounds(startTime = "12:01", finishTime = "12:44")==1
    assert obj.numberOfRounds(startTime = "20:00", finishTime = "06:00")==40
    assert obj.numberOfRounds(startTime = "00:00", finishTime = "23:59")==95
    assert obj.numberOfRounds(startTime = "20:01", finishTime = "06:00")==39
