class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n1 = max(nums)
        nums.index(n1)
        nums.remove(n1)

        n2 = max(nums)
        nums.index(n2)
        nums.remove(n2)

        r = (n1-1) * (n2-1)

        return r