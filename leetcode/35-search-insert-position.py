class Solution(object):
    def searchInsert(self, nums, target):
        value = 0
        for i in range(len(nums)):
            if target == nums[i]:
                value = i
            elif target > nums[i]:
                    value = i + 1
            else:
                pass
        return value
                