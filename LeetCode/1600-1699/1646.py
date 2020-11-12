'''
1646. Get Maximum in Generated Array

2020.11.08 Sunday 14:55
'''

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        nums = [0, 1]
        for i in range(2, n+1):
            if i % 2 == 0:
                nbr = nums[int(i/2)]
            else:
                nbr = nums[int((i-1)/2)] + nums[int((i-1)/2)+1]
            nums.append(nbr)
        return max(nums)

if __name__ == "__main__":
    obj = Solution()
    assert obj.getMaximumGenerated(n=7)==3
    assert obj.getMaximumGenerated(n=2)==1
    assert obj.getMaximumGenerated(n=3)==2
    assert obj.getMaximumGenerated(n=0)==0
    assert obj.getMaximumGenerated(n=1)==1
    assert obj.getMaximumGenerated(n=9)==4
