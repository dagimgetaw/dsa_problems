class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        array = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == len(nums2) - 1:
                        array.append(-1)
                    elif nums1[i] < nums2[j + 1]:
                        array.append(nums2[j + 1])
                    elif nums1[i] > nums2[j + 1]:
                        for k in range(j, len(nums2)):
                            if nums1[i] < nums2[k]:
                                array.append(nums2[k])
                                break
                        else:
                            array.append(-1)

        return array