'''
3280. Convert Date to Binary

2024.09.08 Sunday 13:59
'''


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans = [ bin(int(val))[2:] for val in date.split("-")]
        return "-".join(ans)


if __name__ == "__main__":
    obj = Solution()
    assert obj.convertDateToBinary(date = "2080-02-29") == "100000100000-10-11101"
    assert obj.convertDateToBinary(date = "1900-01-01") == "11101101100-1-1"
