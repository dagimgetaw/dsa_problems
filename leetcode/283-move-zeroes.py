class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1

        return nums