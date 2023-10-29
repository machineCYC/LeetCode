'''
2844. Minimum Operations to Make a Special Number

2023.09.03 Sunday 13:08
'''


class Solution:

    def minimumOperations(self, num = str) -> int:
        def exist_number5(nbr: str):
            """handle 25, 75 case"""
            cnt = 0
            n = len(nbr)
            while True:
                if cnt == n:
                    break

                if int(nbr[-2:]) % 25 == 0:
                    break

                if nbr[-1] == '5':
                    nbr = nbr[:-2] + nbr[-1]
                else:
                    nbr = nbr[:-1]
                cnt += 1
            return cnt

        def exist_number0(nbr: str):
            """handle 00, 50 case"""
            cnt = 0
            n = len(nbr)
            while True:
                if cnt == n:
                    break

                if int(nbr[-2:]) % 25 == 0:
                    break

                if nbr[-1] == '0':
                    nbr = nbr[:-2] + nbr[-1]
                else:
                    nbr = nbr[:-1]
                cnt += 1
            return cnt

        num5 = exist_number5(num)
        num0 = exist_number0(num)
        return min(num5, num0)


if __name__ == "__main__":
    obj = Solution()
    assert obj.minimumOperations(num = "25")==0
    assert obj.minimumOperations(num = "2")==1
    assert obj.minimumOperations(num = "99999")==5
    assert obj.minimumOperations(num = "29083205")==1
    assert obj.minimumOperations(num = "2245047")==2
    assert obj.minimumOperations(num = "2908305")==3
    assert obj.minimumOperations(num = "10")==1
