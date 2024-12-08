'''
3354. Make Array Elements Equal to Zero

2024.11.17 Sunday 23:30
'''
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(curr, direction):
            n = len(nums)
            nums_copy = nums[:]  # Work with a copy to avoid modifying the original array
            while 0 <= curr < n:
                if nums_copy[curr] == 0:
                    curr += direction  # Move in the current direction
                elif nums_copy[curr] > 0:
                    nums_copy[curr] -= 1  # Decrement the value
                    direction = -direction  # Reverse direction
                    curr += direction  # Move in the new direction
                else:
                    break  # Should never happen as nums[curr] >= 0 is guaranteed

            # Check if all elements have become 0
            return all(x == 0 for x in nums_copy)

        valid_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                # Try both directions
                if simulate(i, 1):  # Moving right
                    valid_count += 1
                if simulate(i, -1):  # Moving left
                    valid_count += 1

        return valid_count

if __name__ == "__main__":
    obj = Solution()
    assert obj.countValidSelections(nums = [1,0,2,0,3]) == 2
    assert obj.countValidSelections(nums = [2,3,4,0,4,1,0]) == 0
