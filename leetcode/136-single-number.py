class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                pass
            else:
                n = nums[i]
        return n