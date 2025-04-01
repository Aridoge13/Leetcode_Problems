from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Hash table to store number and its index
        for i, num in enumerate(nums):
            complement = target - num  # Find the complement
            if complement in num_map:
                # Return indices of complement and current number
                return [num_map[complement], i]
            num_map[num] = i  # Store the number with its index
        return []


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 18
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
