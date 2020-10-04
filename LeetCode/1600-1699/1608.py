'''
1608. Special Array With X Elements Greater Than or Equal X

2020.10.04 Sunday 15:15
'''
import typing

class Solution:
    def specialArray(self, nums: typing.List[int]) -> int:
        for n in range(0, max(nums)+1):
            count = 0
            for m in nums:
                if m>=n:
                    count+=1
            if count == n:
                return n
        return -1

if __name__ == "__main__":
    obj = Solution()
    assert obj.specialArray(nums = [3,5])==2
    assert obj.specialArray(nums = [0,0])==-1
    assert obj.specialArray(nums = [0,4,3,0,4])==3
    assert obj.specialArray(nums = [3,6,7,7,0])==-1
    assert obj.specialArray(nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100])==100
