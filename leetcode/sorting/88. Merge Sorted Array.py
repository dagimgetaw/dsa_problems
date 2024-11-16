class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1 = nums1[:m]
        n2 = nums2[:n]

        nums1[:m + n] = n1 + n2  
        nums1.sort()  

        return nums1