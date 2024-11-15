class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        k = 1
        window = nums[:k]
        result = window

        for i in range(k, len(nums)): 
            result = result if len(result) > len(window) else window

            if 0 in window and nums[i] == 0:
                r = window.index(0)
                window = window[r+1:]
                window.append(nums[i])
                result = result if len(result) > len(window) else window
            else:
                window.append(nums[i])
                result = result if len(result) > len(window) else window


        if 0 in result:
            return sum(result)
        else:
            return sum(result) - 1