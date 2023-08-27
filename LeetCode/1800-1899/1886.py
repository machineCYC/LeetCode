'''
1886. Determine Whether Matrix Can Be Obtained By Rotation

2021.06.06 Sunday 14:37
'''
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_mat(mat):
            return [list(i) for i in zip(*mat[::-1])]

        def check_mat_equal(mat, target_mat):
            n = len(mat)
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        return False
            return True

        count = 1
        while count <= 4:
            mat = rotate_mat(mat)
            bool_ret = check_mat_equal(mat, target)
            if bool_ret:
                return True
            count += 1
        return False


if __name__ == "__main__":
    obj = Solution()
    assert obj.findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]) == True
    assert obj.findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]) == False
    assert obj.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]) == True
