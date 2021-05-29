'''
1710. Maximum Units on a Truck

2021.01.03 Sunday 14:00
'''
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        number = 0
        for boxType in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            numberbox, numberunits = boxType
            for i in range(numberbox):
                if count+1 > truckSize:
                    break
                count += 1
                number += numberunits
        return number

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)==8
    assert obj.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)==91
