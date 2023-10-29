'''
2895. Minimum Processing Time

2023.10.08 Sunday 12:22
'''
from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        tasks = tasks[::-1]

        ans = 0
        for idx, p in enumerate(processorTime):
            max_task = idx * 4
            ans = max(ans, p + tasks[max_task])
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.minProcessingTime(processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]) == 16
    assert obj.minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]) == 23
