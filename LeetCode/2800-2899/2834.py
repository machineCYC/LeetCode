'''
2834. Find the Minimum Possible Sum of a Beautiful Array

2023.08.27 Sunday 14:21
'''

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        limit = set()
        ans = []
        i = 1
        cnt = 0
        while True:
            if i not in limit:
                ans.append(i)
                cnt += 1
                limit.add(i)
                limit_nbr = target - i
                if limit_nbr > 0:
                    limit.add(limit_nbr)

            if cnt == n:
                break

            i += 1
        return sum(ans)



if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumPossibleSum(n = 2, target = 3)==4
    assert obj.minimumPossibleSum(n = 3, target = 3)==8
    assert obj.minimumPossibleSum(n = 1, target = 1)==1