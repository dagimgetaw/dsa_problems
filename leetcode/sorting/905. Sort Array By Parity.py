class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []

        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                arr.insert(0, nums[i])
            else:
                arr.insert(len(arr), nums[i])

        return arr