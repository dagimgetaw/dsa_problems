class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x = y = sum(nums[:k])

        for i in range(k, len(nums)):
            x = x + nums[i] - nums[i - k]
            y = max(x, y)

        result = y / k
        return result