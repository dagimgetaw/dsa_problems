class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr = []
        
        for num in arr2:
            while num in arr1:
                arr.append(num)
                arr1.remove(num)
        
        arr += sorted(arr1)
        
        return arr
        