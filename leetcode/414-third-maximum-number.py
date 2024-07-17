class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = list(dict.fromkeys(nums))
        length = len(nums)

        if length < 3:
            result = max(nums)
        else:
            for i in range(2):
                num = max(nums)
                nums.remove(num)
            result = max(nums)

        return result