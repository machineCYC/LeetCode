'''
2279. Maximum Bags With Full Capacity of Rocks

2022.05.22 Sunday 12:44
'''


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = sorted(c - r for c,r in zip(capacity, rocks))[::-1]
        while count and additionalRocks and count[-1] <= additionalRocks:
            additionalRocks -= count.pop()
        return len(rocks) - len(count)

if __name__ == "__main__":
    obj = Solution()
    assert obj.maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2) == 3
    assert obj.maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100) == 3
