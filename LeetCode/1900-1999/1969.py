'''
1969. Minimum Non-Zero Product of the Array Elements

2021.08.15 Sunday 15:33
'''

class Solution:
    '''
    example:
    p = 4
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    each pair (i, 2**p-1) can swap two bits to (1, 2**p-2)
    so the array can finaliy become [1, 1, 1, 1, 1, 1, 1, 14, 14, 14, 14, 14, 14, 14, 15]
    '''
    def minNonZeroProduct(self, p: int) -> int:
        return (pow(2**p -2, 2**(p-1) - 1, 10**9 + 7) * (2**p - 1)) % (10**9 + 7)

if __name__ == "__main__":
    obj = Solution()
    assert obj.minNonZeroProduct(p = 1)==1
    assert obj.minNonZeroProduct(p = 2)==6
    assert obj.minNonZeroProduct(p = 3)==1512