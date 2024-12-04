class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        arr = []

        for num in image:
            num.reverse()
            arr.append(num)

        res = []

        for x in arr:
            temp = []
            for y in x:
                if y == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            res.append(temp)

        return res