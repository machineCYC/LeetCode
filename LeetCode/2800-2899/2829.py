'''
2829. Determine the Minimum Sum of a k-avoiding Array

2023.08.20 Sunday 15:08
'''


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        cnt = 0
        i = 1
        avoids = {0}
        k_avoiding = []
        while True:
            ops_value = max(k - i, i)
            print(ops_value, i)
            if not (i in avoids):
                avoids.add(ops_value)
                k_avoiding.append(i)
                cnt += 1
                print(k_avoiding, avoids, cnt)
                if cnt == (n):
                    return sum(k_avoiding)
            i += 1

if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumSum(n = 5, k = 4) == 18
    assert obj.minimumSum(n = 2, k = 6) == 3
    assert obj.minimumSum(n = 1, k = 1) == 1
