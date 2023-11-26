'''
2946. Matrix Similarity After Cyclic Shifts

2023.11.26 Sunday 14:09
'''
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k = k % n
        for idx, row in enumerate(mat):
            if idx % 2 == 0: # odd index, right shift
                new_row = row[-k:] + row[0:-k]
            else:
                new_row = row[k:] + row[0:k]
            if row != new_row:
                return False
        return True


if __name__ == "__main__":
    obj = Solution()
    assert obj.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2) == True
    assert obj.areSimilar(mat = [[2,2],[2,2]], k = 3) == True
    assert obj.areSimilar(mat = [[1,2]], k = 1) == False
    assert obj.areSimilar(mat = [[6,6,6,6,6,6,6,6,6,6],[9,9,9,9,9,9,9,9,9,9],[1,1,1,1,1,1,1,1,1,1],[10,10,10,10,10,10,10,10,10,10],[2,2,2,2,2,2,2,2,2,2],[6,6,6,6,6,6,6,6,6,6],[7,7,7,7,7,7,7,7,7,7],[9,9,9,9,9,9,9,9,9,9],[8,8,8,8,8,8,8,8,8,8]], k = 1) == True
