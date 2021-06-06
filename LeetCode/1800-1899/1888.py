'''
1888. Minimum Number of Flips to Make the Binary String Alternating

2021.06.06 Sunday 17:21
'''


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        even_index_1_count = 0 # 偶數 index 為 1 個數
        odd_index_1_count = 0 # 偶數 index 為 1 個數
        for i in range(n):
            if i % 2 == 0 and s[i] == '1':
                even_index_1_count += 1

            if i % 2 == 1 and s[i] == '1':
                odd_index_1_count += 1


        if n % 2 == 0:
            # 偶數長度一定一半為 0 另一半為 1
            ans = min(n // 2 + even_index_1_count - odd_index_1_count, n // 2 - even_index_1_count + odd_index_1_count)
        else:
            # 奇數長度在起始為 0 和 1 個數會不同
            ans = min(((n-1) // 2) - odd_index_1_count + even_index_1_count, ((n+1) // 2) + odd_index_1_count - even_index_1_count)

            # 奇數長度必須做 type-2 operation (每個 digit 都做)
            for i in range(n):
                if s[i] == '1':
                    even_index_1_count, odd_index_1_count = odd_index_1_count + 1, even_index_1_count - 1
                else:
                    even_index_1_count, odd_index_1_count = odd_index_1_count, even_index_1_count
                ans = min(ans, min(((n-1) // 2) - odd_index_1_count + even_index_1_count, ((n+1) // 2) + odd_index_1_count - even_index_1_count))
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.minFlips(s = "111000") == 2
    assert obj.minFlips(s = "010") == 0
    assert obj.minFlips(s = "1110") == 1
    assert obj.minFlips(s = "01001001101") == 2
