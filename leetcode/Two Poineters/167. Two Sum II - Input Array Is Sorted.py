class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1
        value = True

        while value:
            if numbers[left] + numbers[right] == target:
                return (left+1, right+1)
                value = False
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
