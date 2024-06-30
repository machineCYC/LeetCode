'''
3200. Maximum Height of a Triangle

2024.06.30 Sunday 14:33
'''


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        max_height = max(red, blue)
        while max_height:
            odd_hight = sum(i for i in range(1, max_height+1, 1) if i % 2 != 0)
            even_hight = sum(i for i in range(1, max_height+1, 1) if i % 2 == 0)

            if (odd_hight<=red and even_hight<=blue) or (odd_hight<=blue and even_hight<=red):
                return max_height

            max_height -= 1


if __name__ == "__main__":
    obj = Solution()
    assert obj.maxHeightOfTriangle(red = 2, blue = 4) == 3
    assert obj.maxHeightOfTriangle(red = 2, blue = 1) == 2
    assert obj.maxHeightOfTriangle(red = 1, blue = 1) == 1
    assert obj.maxHeightOfTriangle(red = 10, blue = 1) == 2
