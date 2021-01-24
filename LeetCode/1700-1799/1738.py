'''
1738. Find Kth Largest XOR Coordinate Value

2021.01.24 Sunday 17:30
'''
from typing import List


matrix = [[5,2],[1,6]]
k = 1

matrix = [[5,2],[1,6]]
k = 2

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        elements = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i-1>=0:
                    matrix[i][j] = matrix[i-1][j] ^ matrix[i][j]
                if j-1>=0:
                    matrix[i][j] = matrix[i][j-1] ^ matrix[i][j]
                if i-1>=0 and j-1>=0:
                    matrix[i][j] = matrix[i-1][j-1] ^ matrix[i][j]

                elements.append(matrix[i][j])
        return sorted(elements)[-k]


if __name__ == "__main__":
    obj = Solution()
    assert obj.kthLargestValue(matrix = [[5,2],[1,6]], k=1)==7
    assert obj.kthLargestValue(matrix = [[5,2],[1,6]], k = 2)==5
    assert obj.kthLargestValue(matrix = [[5,2],[1,6]], k = 3)==4
    assert obj.kthLargestValue(matrix = [[5,2],[1,6]], k = 4)==0
