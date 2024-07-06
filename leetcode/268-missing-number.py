class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sort = sorted(nums)
        initial = 0

        for i in sort:
            if initial == i:
                initial += 1
                
        return initial