class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        arr = []
        res = [0]*len(score)

        for i in score:
            arr.append(i)

        for i in range(len(score)):
            n = max(arr)
            m = score.index(n)
            res[m] = i
            arr.remove(n)

        arr.clear()
        arr = []

        for i in range(len(res)):
            if res[i] == 0:
                arr.append("Gold Medal")
            elif res[i] == 1:
                arr.append("Silver Medal")
            elif res[i] == 2:
                arr.append("Bronze Medal")
            else:
                arr.append(str(res[i]+1))

        return arr
