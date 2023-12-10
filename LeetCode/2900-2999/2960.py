'''
2960. Count Tested Devices After Test Operations

2023.12.10 Sunday 14:04
'''
from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        test_cnt = 0
        for p in batteryPercentages:
            if max(0, (p - test_cnt)) ==  0:
                pass
            else:
                test_cnt += 1
                ans += 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.countTestedDevices(batteryPercentages = [1,1,2,1,3]) == 3
    assert obj.countTestedDevices(batteryPercentages = [0,1,2]) == 2
    assert obj.countTestedDevices(batteryPercentages = [1,0]) == 1