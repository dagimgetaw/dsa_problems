class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        arr = []

        for i in nums:
            if i < 0:
                arr.append(i*-1)
            else:
                arr.append(i)

        arr.sort()
        for i in range(len(arr)):
            arr[i] = arr[i] ** 2

        return arr