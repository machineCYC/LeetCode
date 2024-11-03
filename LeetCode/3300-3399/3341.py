'''
3341. Find Minimum Time to Reach Last Room I

2024.11.03 Sunday 18:40
'''
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        min_time = [[float('inf')] * m for _ in range(n)]  # minimum time to reach each cell
        min_time[0][0] = 0
        heap = [(0, 0, 0)]  # (time, row, col)

        while heap:
            current_time, x, y = heapq.heappop(heap)

            # If we've reached the bottom-right room, return the time
            if x == n - 1 and y == m - 1:
                return current_time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check bounds
                if 0 <= nx < n and 0 <= ny < m:
                    # Calculate the earliest we can enter the next room
                    wait_time = max(moveTime[nx][ny], current_time) + 1

                    # If wait time + 1 second to enter next room is less than current recorded time
                    if wait_time < min_time[nx][ny]:
                        min_time[nx][ny] = wait_time
                        heapq.heappush(heap, (wait_time, nx, ny))

        # If we exhaust the heap without reaching the target, return -1 (impossible case)
        return -1

if __name__ == "__main__":
    obj = Solution()
    assert obj.minTimeToReach(moveTime = [[0,4],[4,4]]) == 6
    assert obj.minTimeToReach(moveTime = [[0,0,0],[0,0,0]]) == 3
    assert obj.minTimeToReach(moveTime = [[0,1],[1,2]]) == 3
