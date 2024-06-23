class Solution:
    def majorityElement(self, nums: List[int]) -> int:       
        from collections import Counter

        most_common_element = Counter(nums).most_common(1)[0][0]
        return most_common_element