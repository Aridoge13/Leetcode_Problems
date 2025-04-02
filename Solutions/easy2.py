from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # Precompute max_left: max(nums[0..i-1])
        max_left = [0] * n
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], nums[i-1])

        # Precompute max_right: max(nums[i+1..n-1])
        max_right = [0] * n
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], nums[i+1])

        max_value = 0
        for j in range(1, n-1):  # j ranges from 1 to n-2 (i < j < k)
            current = (max_left[j] - nums[j]) * max_right[j]
            if current > max_value:
                max_value = current

        return max_value if max_value > 0 else 0


if __name__ == "__main__":
    solution = Solution()
    nums = [12, 6, 1, 2, 7]
    print(solution.maximumTripletValue(nums))
